from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from config import mysql
from routes.analytics import record_view
import os

gallery_bp = Blueprint("gallery", __name__)

UPLOAD_FOLDER = "static/uploads/gallery"


# =====================================================
# PUBLIC GALLERY
# =====================================================

@gallery_bp.route("/gallery")
def gallery():

    record_view("Gallery")

    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT id, title, image
        FROM gallery
        ORDER BY id DESC
    """)

    photos = cur.fetchall()

    cur.close()

    # -----------------------------------------
    # Group photos according to title
    # -----------------------------------------

    gallery_groups = {}

    for photo in photos:

        photo_id = photo[0]
        title = photo[1]
        image = photo[2]

        if title not in gallery_groups:
            gallery_groups[title] = []

        gallery_groups[title].append({
            "id": photo_id,
            "image": image
        })

    return render_template(
        "gallery.html",
        gallery_groups=gallery_groups
    )


# =====================================================
# UPLOAD MULTIPLE PHOTOS
# =====================================================

@gallery_bp.route("/gallery/upload", methods=["GET", "POST"])
def gallery_upload():

    if request.method == "POST":

        title = request.form.get("title", "").strip()

        images = request.files.getlist("images")

        if not title:
            flash("Please enter gallery title.")
            return redirect("/gallery/upload")

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        cur = mysql.connection.cursor()

        uploaded = 0

        for image in images:

            if image and image.filename:

                filename = secure_filename(image.filename)

                image_path = os.path.join(
                    UPLOAD_FOLDER,
                    filename
                )

                image.save(image_path)

                cur.execute("""
                    INSERT INTO gallery
                    (title, image)
                    VALUES (%s, %s)
                """, (title, filename))

                uploaded += 1

        mysql.connection.commit()

        cur.close()

        flash(
            f"{uploaded} photos uploaded successfully!"
        )

        return redirect("/gallery")

    return render_template(
        "gallery_upload.html"
    )


# =====================================================
# MANAGE GALLERY
# =====================================================

@gallery_bp.route("/gallery/manage")
def gallery_manage():

    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT id, title, image
        FROM gallery
        ORDER BY id DESC
    """)

    photos = cur.fetchall()

    cur.close()

    return render_template(
        "gallery_manage.html",
        photos=photos
    )


# =====================================================
# EDIT GALLERY IMAGE
# =====================================================

@gallery_bp.route(
    "/gallery/edit/<int:id>",
    methods=["GET", "POST"]
)
def gallery_edit(id):

    cur = mysql.connection.cursor()

    if request.method == "POST":

        title = request.form.get("title", "").strip()

        image = request.files.get("image")

        # -----------------------------------------
        # If new image selected
        # -----------------------------------------

        if image and image.filename:

            filename = secure_filename(
                image.filename
            )

            os.makedirs(
                UPLOAD_FOLDER,
                exist_ok=True
            )

            image.save(
                os.path.join(
                    UPLOAD_FOLDER,
                    filename
                )
            )

            cur.execute("""
                UPDATE gallery
                SET title=%s, image=%s
                WHERE id=%s
            """, (title, filename, id))

        # -----------------------------------------
        # Only title changed
        # -----------------------------------------

        else:

            cur.execute("""
                UPDATE gallery
                SET title=%s
                WHERE id=%s
            """, (title, id))

        mysql.connection.commit()

        cur.close()

        flash("Gallery updated successfully!")

        return redirect("/gallery/manage")

    # GET request

    cur.execute("""
        SELECT id, title, image
        FROM gallery
        WHERE id=%s
    """, (id,))

    photo = cur.fetchone()

    cur.close()

    return render_template(
        "gallery_edit.html",
        photo=photo
    )


# =====================================================
# DELETE GALLERY IMAGE
# =====================================================

@gallery_bp.route("/gallery/delete/<int:id>")
def gallery_delete(id):

    cur = mysql.connection.cursor()

    # First get image filename

    cur.execute("""
        SELECT image
        FROM gallery
        WHERE id=%s
    """, (id,))

    result = cur.fetchone()

    if result:

        filename = result[0]

        # Delete database record

        cur.execute("""
            DELETE FROM gallery
            WHERE id=%s
        """, (id,))

        mysql.connection.commit()

        # Delete physical image

        image_path = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        if os.path.exists(image_path):
            os.remove(image_path)

    cur.close()

    flash("Gallery image deleted successfully!")

    return redirect("/gallery/manage")