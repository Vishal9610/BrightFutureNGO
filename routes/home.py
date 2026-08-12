from flask import Blueprint, render_template
from config import mysql
from routes.analytics import record_view

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    
    print("HOME ROUTE RUNNING")
    record_view("Home")


    cur = mysql.connection.cursor()

    # Latest News
    cur.execute("SELECT * FROM news ORDER BY news_date DESC LIMIT 3")
    news = cur.fetchall()

    # Latest Gallery Images
    cur.execute("SELECT * FROM gallery ORDER BY id DESC LIMIT 6")
    photos = cur.fetchall()

    # Team Members
    cur.execute("SELECT * FROM team LIMIT 3")
    members = cur.fetchall()

    cur.close()

    return render_template(
        "index.html",
        news=news,
        photos=photos,
        members=members
    )
@home_bp.route("/about")
def about():

    record_view("About")

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM partners ORDER BY id DESC")

    partners = cur.fetchall()

    cur.close()

    return render_template(
        "about.html",
        partners=partners
    )

@home_bp.route("/programs")
def programs():

    record_view("Programs")

    return render_template("programs.html")

from config import mysql

gallery_bp = Blueprint("gallery", __name__)

@gallery_bp.route("/gallery")
def gallery():

    record_view("Gallery")

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM gallery ORDER BY id DESC")

    photos = cur.fetchall()

    cur.close()

    return render_template("gallery.html", photos=photos)



#Contact Details

from flask import request, redirect

from config import mysql



@home_bp.route("/contact", methods=["GET", "POST"])
def contact():


    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        cur = mysql.connection.cursor()

        cur.execute(
            """
            INSERT INTO contact
            (name,email,subject,message)

            VALUES(%s,%s,%s,%s)
            """,
            (name,email,subject,message)
        )

        mysql.connection.commit()

        cur.close()

        return redirect("/contact")
    
    record_view("Contact")

    return render_template("contact.html")

@home_bp.route("/donate")
def donate():

    record_view("Donate")

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM donation WHERE id=1")

    donation = cur.fetchone()

    cur.close()

    return render_template(
        "donate.html",
        donation=donation
    )

@home_bp.route("/learn-more")
def learn_more():

    record_view("Learn More")

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM partners ORDER BY id DESC")

    partners = cur.fetchall()

    cur.close()

    return render_template(
        "learn_more.html",
        partners=partners
    )


@home_bp.route("/team")
def team():

    record_view("Team")

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM team")

    members = cur.fetchall()

    cur.close()

    return render_template(
        "team.html",
        members=members
    )


@home_bp.route("/about-details")
def about_details():

    record_view("About Details")

    return render_template("about_details.html")
