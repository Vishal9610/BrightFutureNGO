from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from config import mysql

from werkzeug.utils import secure_filename

import os

gallery_bp = Blueprint("gallery",__name__)

@gallery_bp.route("/gallery/upload",methods=["GET","POST"])
def gallery_upload():

    if request.method=="POST":

        title=request.form["title"]

        image=request.files["image"]

        filename=secure_filename(image.filename)

        image.save(

            os.path.join(
                "static/uploads/gallery",
                filename
            )

        )

        cur=mysql.connection.cursor()

        cur.execute(

            "INSERT INTO gallery(title,image) VALUES(%s,%s)",

            (title,filename)

        )

        mysql.connection.commit()

        cur.close()

        return redirect("/gallery/manage")

    return render_template("gallery_upload.html")


@gallery_bp.route("/gallery/manage")
def manage_gallery():

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM gallery ORDER BY id DESC")

    photos = cur.fetchall()

    cur.close()

    return render_template(
        "manage_gallery.html",
        photos=photos
    )

@gallery_bp.route("/gallery/edit/<int:id>", methods=["GET", "POST"])
def edit_gallery(id):

    cur = mysql.connection.cursor()

    if request.method == "POST":

        title = request.form["title"]

        image = request.files["image"]

        if image.filename != "":

            filename = secure_filename(image.filename)

            image.save(
                os.path.join(
                    "static/uploads/gallery",
                    filename
                )
            )

            cur.execute(
                "UPDATE gallery SET title=%s, image=%s WHERE id=%s",
                (title, filename, id)
            )

        else:

            cur.execute(
                "UPDATE gallery SET title=%s WHERE id=%s",
                (title, id)
            )

        mysql.connection.commit()

        cur.close()

        return redirect("/gallery/manage")

    cur.execute("SELECT * FROM gallery WHERE id=%s", (id,))

    photo = cur.fetchone()

    cur.close()

    return render_template(
        "edit_gallery.html",
        photo=photo
    )

@gallery_bp.route("/gallery/delete/<int:id>")
def delete_gallery(id):

    cur = mysql.connection.cursor()

    cur.execute(
        "DELETE FROM gallery WHERE id=%s",
        (id,)
    )

    mysql.connection.commit()

    cur.close()

    return redirect("/gallery/manage")