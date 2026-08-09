from flask import Blueprint, render_template, request, redirect, session, flash
from werkzeug.utils import secure_filename
import os
from config import mysql

admin_bp = Blueprint("admin", __name__)

# Admin Login
@admin_bp.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        cur = mysql.connection.cursor()

        cur.execute(
            "SELECT * FROM admin WHERE username=%s AND password=%s",
            (username, password)
        )

        admin = cur.fetchone()

        cur.close()

        if admin:

            session["admin"] = username

            return redirect("/dashboard")

        else:

            flash("Invalid Username or Password")

    return render_template("admin_login.html")

# Dashboard

@admin_bp.route("/dashboard")
def dashboard():

    if "admin" not in session:

        return redirect("/admin")

    cur = mysql.connection.cursor()

    # Count Gallery Images
    cur.execute("SELECT COUNT(*) FROM gallery")
    gallery_count = cur.fetchone()[0]

    # Count Contact Messages
    cur.execute("SELECT COUNT(*) FROM contact")
    message_count = cur.fetchone()[0]

    cur.close()

    return render_template(
        "dashboard.html",
        gallery_count=gallery_count,
        message_count=message_count
    )

# Logout

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

