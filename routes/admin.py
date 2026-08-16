# from flask import Blueprint, render_template, request, redirect, session, flash
# from werkzeug.utils import secure_filename
# import os
# from config import mysql
import random
import os

from flask import Blueprint, render_template, request, redirect, session, flash
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from config import mysql, mail


admin_bp = Blueprint("admin", __name__)


# =========================================================
# ADMIN LOGIN
# =========================================================

@admin_bp.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:

            flash("Username and Password are required.")

            return redirect("/admin")

        cur = mysql.connection.cursor()

        cur.execute(
            """
            SELECT *
            FROM admin
            WHERE username=%s
            """,
            (username,)
        )

        admin_user = cur.fetchone()

        cur.close()

        if admin_user:

            stored_password = admin_user[2]

            try:

                password_correct = check_password_hash(
                    stored_password,
                    password
                )

            except ValueError:

                # Old plain-text password support
                password_correct = (
                    stored_password == password
                )

            if password_correct:

                session["admin"] = username

                return redirect("/dashboard")

        flash("Invalid Username or Password.")

    return render_template("admin_login.html")


# =========================================================
# FORGOT USERNAME
# =========================================================

@admin_bp.route("/forgot-username", methods=["GET", "POST"])
def forgot_username():

    if request.method == "POST":

        contact = request.form.get("contact", "").strip()

        if not contact:

            flash("Please enter your email or mobile number.")

            return redirect("/forgot-username")

        cur = mysql.connection.cursor()

        cur.execute(
            """
            SELECT id, username, email, mobile
            FROM admin
            WHERE email=%s OR mobile=%s
            """,
            (contact, contact)
        )

        admin_user = cur.fetchone()

        cur.close()

        if not admin_user:

            flash(
                "No admin account found with this email or mobile number."
            )

            return redirect("/forgot-username")

        admin_id = admin_user[0]
        username = admin_user[1]
        email = admin_user[2]

        if not email:

            flash(
                "No email address is registered for this admin account."
            )

            return redirect("/forgot-username")

        # Generate OTP
        otp = str(random.randint(100000, 999999))

        session["forgot_username_otp"] = otp
        session["forgot_username_admin_id"] = admin_id
        session["forgot_username_value"] = username

        try:

            msg = Message(
                subject="Bright Future Foundation - Username Recovery",
                sender=mail.username,
                recipients=[email]
            )

            msg.body = f"""
Hello,

Your Bright Future Foundation username recovery OTP is:

{otp}

This OTP is valid for this recovery session.

If you did not request this, please ignore this email.

Regards,
Bright Future Foundation
"""

            mail.send(msg)

            flash("OTP has been sent to your registered email.")

            return redirect("/verify-username-otp")

        except Exception as e:

            print("================================")
            print("EMAIL ERROR:")
            print(e)
            print("================================")

            flash(
                "Unable to send OTP. Please check Gmail configuration."
            )

            return redirect("/forgot-username")

    return render_template("forgot_username.html")


# =========================================================
# VERIFY USERNAME OTP
# =========================================================

@admin_bp.route("/verify-username-otp", methods=["GET", "POST"])
def verify_username_otp():

    if "forgot_username_otp" not in session:

        return redirect("/forgot-username")

    if request.method == "POST":

        entered_otp = request.form.get("otp", "").strip()

        actual_otp = session.get("forgot_username_otp")

        if entered_otp == actual_otp:

            username = session.get("forgot_username_value")

            session.pop("forgot_username_otp", None)
            session.pop("forgot_username_admin_id", None)
            session.pop("forgot_username_value", None)

            return render_template(
                "username_result.html",
                username=username
            )

        flash("Invalid OTP.")

    return render_template("verify_username_otp.html")


# =========================================================
# FORGOT PASSWORD
# =========================================================

@admin_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        contact = request.form.get("contact", "").strip()

        if not contact:

            flash("Please enter your email or mobile number.")

            return redirect("/forgot-password")

        cur = mysql.connection.cursor()

        cur.execute(
            """
            SELECT id, username, email, mobile
            FROM admin
            WHERE email=%s OR mobile=%s
            """,
            (contact, contact)
        )

        admin_user = cur.fetchone()

        cur.close()

        if not admin_user:

            flash(
                "No admin account found with this email or mobile number."
            )

            return redirect("/forgot-password")

        admin_id = admin_user[0]
        email = admin_user[2]

        if not email:

            flash(
                "No email address is registered for this admin account."
            )

            return redirect("/forgot-password")

        # Generate OTP
        otp = str(random.randint(100000, 999999))

        session["forgot_password_otp"] = otp
        session["forgot_password_admin_id"] = admin_id

        try:

            msg = Message(
                subject="Bright Future Foundation - Password Reset",
                sender=mail.username,
                recipients=[email]
            )

            msg.body = f"""
Hello,

Your password reset OTP is:

{otp}

Use this OTP to reset your admin password.

If you did not request this password reset, please ignore this email.

Regards,
Bright Future Foundation
"""

            mail.send(msg)

            flash("OTP has been sent to your registered email.")

            return redirect("/verify-password-otp")

        except Exception as e:

            print("================================")
            print("EMAIL ERROR:")
            print(e)
            print("================================")

            flash(
                "Unable to send OTP. Please check Gmail configuration."
            )

            return redirect("/forgot-password")

    return render_template("forgot_password.html")


# =========================================================
# VERIFY PASSWORD OTP
# =========================================================

@admin_bp.route("/verify-password-otp", methods=["GET", "POST"])
def verify_password_otp():

    if "forgot_password_otp" not in session:

        return redirect("/forgot-password")

    if request.method == "POST":

        entered_otp = request.form.get("otp", "").strip()

        actual_otp = session.get("forgot_password_otp")

        if entered_otp == actual_otp:

            session["password_otp_verified"] = True

            return redirect("/reset-password")

        flash("Invalid OTP.")

    return render_template("verify_password_otp.html")


# =========================================================
# RESET PASSWORD
# =========================================================

@admin_bp.route("/reset-password", methods=["GET", "POST"])
def reset_password():

    if not session.get("password_otp_verified"):

        return redirect("/forgot-password")

    admin_id = session.get("forgot_password_admin_id")

    if not admin_id:

        return redirect("/forgot-password")

    if request.method == "POST":

        new_password = request.form.get("password", "")
        confirm_password = request.form.get(
            "confirm_password",
            ""
        )

        if not new_password or not confirm_password:

            flash("Please fill both password fields.")

            return redirect("/reset-password")

        if new_password != confirm_password:

            flash("Passwords do not match.")

            return redirect("/reset-password")

        if len(new_password) < 6:

            flash(
                "Password must contain at least 6 characters."
            )

            return redirect("/reset-password")

        password_hash = generate_password_hash(
            new_password
        )

        cur = mysql.connection.cursor()

        cur.execute(
            """
            UPDATE admin
            SET password=%s
            WHERE id=%s
            """,
            (password_hash, admin_id)
        )

        mysql.connection.commit()

        cur.close()

        # Clear recovery session
        session.pop("forgot_password_otp", None)
        session.pop("forgot_password_admin_id", None)
        session.pop("password_otp_verified", None)

        flash(
            "Password reset successfully. Please login."
        )

        return redirect("/admin")

    return render_template("reset_password.html")


# =========================================================
# DASHBOARD
# =========================================================

@admin_bp.route("/dashboard")
def dashboard():

    if "admin" not in session:

        return redirect("/admin")

    cur = mysql.connection.cursor()

    cur.execute("SELECT COUNT(*) FROM gallery")
    gallery_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM contact")
    message_count = cur.fetchone()[0]

    cur.close()

    return render_template(
        "dashboard.html",
        gallery_count=gallery_count,
        message_count=message_count
    )


# =========================================================
# LOGOUT
# =========================================================

@admin_bp.route("/logout")
def logout():

    session.pop("admin", None)

    return redirect("/admin")

#donation update

from werkzeug.utils import secure_filename
import os

@admin_bp.route("/manage-donation", methods=["GET", "POST"])
def manage_donation():

    if "admin" not in session:
        return redirect("/admin")

    cur = mysql.connection.cursor()

    if request.method == "POST":

        upi = request.form["upi_id"]
        account = request.form["account_name"]
        bank = request.form["bank_name"]
        number = request.form["account_number"]
        ifsc = request.form["ifsc_code"]

        image = request.files["qr_code"]

        if image and image.filename != "":

            filename = secure_filename(image.filename)

            image.save(
                os.path.join("static", "images", filename)
            )

            cur.execute("""
                UPDATE donation
                SET
                    upi_id=%s,
                    account_name=%s,
                    bank_name=%s,
                    account_number=%s,
                    ifsc_code=%s,
                    qr_code=%s
                WHERE id=1
            """, (upi, account, bank, number, ifsc, filename))

        else:

            cur.execute("""
                UPDATE donation
                SET
                    upi_id=%s,
                    account_name=%s,
                    bank_name=%s,
                    account_number=%s,
                    ifsc_code=%s
                WHERE id=1
            """, (upi, account, bank, number, ifsc))

        mysql.connection.commit()

        cur.close()

        return redirect("/manage-donation")

    cur.execute("SELECT * FROM donation WHERE id=1")
    donation = cur.fetchone()
    cur.close()

    return render_template(
        "manage_donation.html",
        donation=donation
    )


#Massage Details

@admin_bp.route("/messages")
def messages():

    if "admin" not in session:

        return redirect("/admin")

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM contact ORDER BY id DESC")

    messages = cur.fetchall()

    cur.close()

    return render_template(
        "messages.html",
        messages=messages
    )


from flask import request, render_template, redirect
from config import mysql

@admin_bp.route("/manage-news", methods=["GET","POST"])
def manage_news():

    if "admin" not in session:
        return redirect("/admin")

    cur = mysql.connection.cursor()

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        news_date = request.form["news_date"]

        cur.execute(
            """
            INSERT INTO news(title,description,news_date)
            VALUES(%s,%s,%s)
            """,
            (title, description, news_date)
        )

        mysql.connection.commit()

        return redirect("/manage-news")

    cur.execute("SELECT * FROM news ORDER BY id DESC")

    news = cur.fetchall()

    cur.close()

    return render_template(
        "manage_news.html",
        news=news
    )

@admin_bp.route("/delete-news/<int:id>")
def delete_news(id):

    if "admin" not in session:
        return redirect("/admin")

    cur = mysql.connection.cursor()

    cur.execute(
        "DELETE FROM news WHERE id=%s",
        (id,)
    )

    mysql.connection.commit()

    cur.close()

    return redirect("/manage-news")

@admin_bp.route("/edit-news/<int:id>", methods=["GET","POST"])
def edit_news(id):

    if "admin" not in session:
        return redirect("/admin")

    cur = mysql.connection.cursor()

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        news_date = request.form["news_date"]

        cur.execute(
            """
            UPDATE news
            SET
            title=%s,
            description=%s,
            news_date=%s
            WHERE id=%s
            """,
            (title, description, news_date, id)
        )

        mysql.connection.commit()

        return redirect("/manage-news")

    cur.execute(
        "SELECT * FROM news WHERE id=%s",
        (id,)
    )

    news = cur.fetchone()

    cur.close()

    return render_template(
        "edit_news.html",
        news=news
    )

from werkzeug.utils import secure_filename
import os

@admin_bp.route("/manage-team", methods=["GET", "POST"])
def manage_team():

    if "admin" not in session:
        return redirect("/admin")

    cur = mysql.connection.cursor()

    if request.method == "POST":

        name = request.form["name"]
        designation = request.form["designation"]
        description = request.form["description"]

        image = request.files["image"]

        filename = ""

        if image.filename != "":
            filename = secure_filename(image.filename)
            image.save(os.path.join("static/images", filename))

        cur.execute("""
        INSERT INTO team(name,designation,image,description)
        VALUES(%s,%s,%s,%s)
        """,(name,designation,filename,description))

        mysql.connection.commit()

        return redirect("/manage-team")

    cur.execute("SELECT * FROM team ORDER BY id DESC")

    members = cur.fetchall()

    cur.close()

    return render_template(
        "manage_team.html",
        members=members
    )

@admin_bp.route("/delete-team/<int:id>")
def delete_team(id):

    if "admin" not in session:
        return redirect("/admin")

    cur = mysql.connection.cursor()

    cur.execute("DELETE FROM team WHERE id=%s",(id,))

    mysql.connection.commit()

    cur.close()

    return redirect("/manage-team")

@admin_bp.route("/edit-team/<int:id>", methods=["GET","POST"])
def edit_team(id):

    if "admin" not in session:
        return redirect("/admin")

    cur = mysql.connection.cursor()

    if request.method=="POST":

        name=request.form["name"]
        designation=request.form["designation"]
        description=request.form["description"]

        image=request.files["image"]

        if image.filename!="":

            filename=secure_filename(image.filename)

            image.save(os.path.join("static/images",filename))

            cur.execute("""
            UPDATE team
            SET
            name=%s,
            designation=%s,
            image=%s,
            description=%s
            WHERE id=%s
            """,(name,designation,filename,description,id))

        else:

            cur.execute("""
            UPDATE team
            SET
            name=%s,
            designation=%s,
            description=%s
            WHERE id=%s
            """,(name,designation,description,id))

        mysql.connection.commit()

        return redirect("/manage-team")

    cur.execute("SELECT * FROM team WHERE id=%s",(id,))

    member=cur.fetchone()

    cur.close()

    return render_template(
        "edit_team.html",
        member=member)

# PARTNERS & SUPPORTERS

from werkzeug.utils import secure_filename
import os


@admin_bp.route("/partner/add", methods=["GET", "POST"])
def add_partner():

    if "admin" not in session:
        return redirect("/admin")

    if request.method == "POST":

        name = request.form["name"]

        image = request.files.get("image")

        if not image or image.filename == "":
            return "Please select an image"

        filename = secure_filename(image.filename)

        upload_folder = os.path.join(
            "static",
            "images"
        )

        os.makedirs(upload_folder, exist_ok=True)

        image.save(
            os.path.join(
                upload_folder,
                filename
            )
        )

        cur = mysql.connection.cursor()

        cur.execute(
            """
            INSERT INTO partners (name, image)
            VALUES (%s, %s)
            """,
            (name, filename)
        )

        mysql.connection.commit()

        cur.close()

        return redirect("/partner/manage")

    return render_template("add_partner.html")


@admin_bp.route("/partner/manage")
def manage_partner():

    if "admin" not in session:
        return redirect("/admin")

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT * FROM partners ORDER BY id DESC"
    )

    partners = cur.fetchall()

    cur.close()

    return render_template(
        "manage_partner.html",
        partners=partners
    )


@admin_bp.route(
    "/partner/edit/<int:id>",
    methods=["GET", "POST"]
)
def edit_partner(id):

    if "admin" not in session:
        return redirect("/admin")

    cur = mysql.connection.cursor()

    if request.method == "POST":

        name = request.form["name"]

        image = request.files.get("image")

        if image and image.filename != "":

            filename = secure_filename(
                image.filename
            )

            upload_folder = os.path.join(
                "static",
                "images"
            )

            os.makedirs(
                upload_folder,
                exist_ok=True
            )

            image.save(
                os.path.join(
                    upload_folder,
                    filename
                )
            )

            cur.execute(
                """
                UPDATE partners
                SET name=%s, image=%s
                WHERE id=%s
                """,
                (name, filename, id)
            )

        else:

            cur.execute(
                """
                UPDATE partners
                SET name=%s
                WHERE id=%s
                """,
                (name, id)
            )

        mysql.connection.commit()

        cur.close()

        return redirect("/partner/manage")

    cur.execute(
        "SELECT * FROM partners WHERE id=%s",
        (id,)
    )

    partner = cur.fetchone()

    cur.close()

    return render_template(
        "edit_partner.html",
        partner=partner
    )


@admin_bp.route("/partner/delete/<int:id>")
def delete_partner(id):

    if "admin" not in session:
        return redirect("/admin")

    cur = mysql.connection.cursor()

    cur.execute(
        "DELETE FROM partners WHERE id=%s",
        (id,)
    )

    mysql.connection.commit()

    cur.close()

    return redirect("/partner/manage")

