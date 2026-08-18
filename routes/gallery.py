# from flask import Blueprint, render_template, request, redirect, flash
# from werkzeug.utils import secure_filename
# from config import mysql
# from routes.analytics import record_view
# import os

# gallery_bp = Blueprint("gallery", __name__)

# UPLOAD_FOLDER = "static/uploads/gallery"


# # =====================================================
# # PUBLIC GALLERY
# # =====================================================

# @gallery_bp.route("/gallery")
# def gallery():

#     record_view("Gallery")

#     cur = mysql.connection.cursor()

#     cur.execute("""
#         SELECT id, title, image
#         FROM gallery
#         ORDER BY id DESC
#     """)

#     photos = cur.fetchall()

#     cur.close()

#     # -----------------------------------------
#     # Group photos according to title
#     # -----------------------------------------

#     gallery_groups = {}

#     for photo in photos:

#         photo_id = photo[0]
#         title = photo[1]
#         image = photo[2]

#         if title not in gallery_groups:
#             gallery_groups[title] = []

#         gallery_groups[title].append({
#             "id": photo_id,
#             "image": image
#         })

#     return render_template(
#         "gallery.html",
#         gallery_groups=gallery_groups
#     )


# # =====================================================
# # UPLOAD MULTIPLE PHOTOS
# # =====================================================

# @gallery_bp.route("/gallery/upload", methods=["GET", "POST"])
# def gallery_upload():

#     if request.method == "POST":

#         title = request.form.get("title", "").strip()

#         images = request.files.getlist("images")

#         if not title:
#             flash("Please enter gallery title.")
#             return redirect("/gallery/upload")

#         os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#         cur = mysql.connection.cursor()

#         uploaded = 0

#         for image in images:

#             if image and image.filename:

#                 filename = secure_filename(image.filename)

#                 image_path = os.path.join(
#                     UPLOAD_FOLDER,
#                     filename
#                 )

#                 image.save(image_path)

#                 cur.execute("""
#                     INSERT INTO gallery
#                     (title, image)
#                     VALUES (%s, %s)
#                 """, (title, filename))

#                 uploaded += 1

#         mysql.connection.commit()

#         cur.close()

#         flash(
#             f"{uploaded} photos uploaded successfully!"
#         )

#         return redirect("/gallery")

#     return render_template(
#         "gallery_upload.html"
#     )


# # =====================================================
# # MANAGE GALLERY
# # =====================================================

# @gallery_bp.route("/gallery/manage")
# def gallery_manage():

#     cur = mysql.connection.cursor()

#     cur.execute("""
#         SELECT id, title, image
#         FROM gallery
#         ORDER BY id DESC
#     """)

#     photos = cur.fetchall()

#     cur.close()

#     return render_template(
#         "gallery_manage.html",
#         photos=photos
#     )


# # =====================================================
# # EDIT GALLERY IMAGE
# # =====================================================

# @gallery_bp.route(
#     "/gallery/edit/<int:id>",
#     methods=["GET", "POST"]
# )
# def gallery_edit(id):

#     cur = mysql.connection.cursor()

#     if request.method == "POST":

#         title = request.form.get("title", "").strip()

#         image = request.files.get("image")

#         # -----------------------------------------
#         # If new image selected
#         # -----------------------------------------

#         if image and image.filename:

#             filename = secure_filename(
#                 image.filename
#             )

#             os.makedirs(
#                 UPLOAD_FOLDER,
#                 exist_ok=True
#             )

#             image.save(
#                 os.path.join(
#                     UPLOAD_FOLDER,
#                     filename
#                 )
#             )

#             cur.execute("""
#                 UPDATE gallery
#                 SET title=%s, image=%s
#                 WHERE id=%s
#             """, (title, filename, id))

#         # -----------------------------------------
#         # Only title changed
#         # -----------------------------------------

#         else:

#             cur.execute("""
#                 UPDATE gallery
#                 SET title=%s
#                 WHERE id=%s
#             """, (title, id))

#         mysql.connection.commit()

#         cur.close()

#         flash("Gallery updated successfully!")

#         return redirect("/gallery/manage")

#     # GET request

#     cur.execute("""
#         SELECT id, title, image
#         FROM gallery
#         WHERE id=%s
#     """, (id,))

#     photo = cur.fetchone()

#     cur.close()

#     return render_template(
#         "gallery_edit.html",
#         photo=photo
#     )


# # =====================================================
# # DELETE GALLERY IMAGE
# # =====================================================

# @gallery_bp.route("/gallery/delete/<int:id>")
# def gallery_delete(id):

#     cur = mysql.connection.cursor()

#     # First get image filename

#     cur.execute("""
#         SELECT image
#         FROM gallery
#         WHERE id=%s
#     """, (id,))

#     result = cur.fetchone()

#     if result:

#         filename = result[0]

#         # Delete database record

#         cur.execute("""
#             DELETE FROM gallery
#             WHERE id=%s
#         """, (id,))

#         mysql.connection.commit()

#         # Delete physical image

#         image_path = os.path.join(
#             UPLOAD_FOLDER,
#             filename
#         )

#         if os.path.exists(image_path):
#             os.remove(image_path)

#     cur.close()

#     flash("Gallery image deleted successfully!")

#     return redirect("/gallery/manage")







import os
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename

from config import mysql, Config
from routes.analytics import record_view

import cloudinary
import cloudinary.uploader
import cloudinary.api


gallery_bp = Blueprint("gallery", __name__)


# =====================================================
# CLOUDINARY CONFIGURATION
# =====================================================

cloudinary.config(
    cloud_name=Config.CLOUDINARY_CLOUD_NAME,
    api_key=Config.CLOUDINARY_API_KEY,
    api_secret=Config.CLOUDINARY_API_SECRET,
    secure=True
)


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

@gallery_bp.route(
    "/gallery/upload",
    methods=["GET", "POST"]
)
def gallery_upload():

    if request.method == "POST":

        title = request.form.get(
            "title",
            ""
        ).strip()

        images = request.files.getlist(
            "images"
        )

        if not title:

            flash(
                "Please enter gallery title."
            )

            return redirect(
                "/gallery/upload"
            )

        uploaded = 0

        cur = mysql.connection.cursor()

        try:

            for image in images:

                if image and image.filename:

                    # ---------------------------------
                    # Upload to Cloudinary
                    # ---------------------------------

                    result = cloudinary.uploader.upload(
                        image,
                        folder="brightfuture/gallery"
                    )

                    image_url = result.get(
                        "secure_url"
                    )

                    if not image_url:
                        continue

                    # ---------------------------------
                    # Save Cloudinary URL in database
                    # ---------------------------------

                    cur.execute("""
                        INSERT INTO gallery
                        (title, image)
                        VALUES (%s, %s)
                    """, (
                        title,
                        image_url
                    ))

                    uploaded += 1

            mysql.connection.commit()

            flash(
                f"{uploaded} photos uploaded successfully!"
            )

        except Exception as e:

            mysql.connection.rollback()

            print(
                "Cloudinary upload error:",
                e
            )

            flash(
                "Gallery upload failed. Please try again."
            )

        finally:

            cur.close()

        return redirect(
            "/gallery"
        )

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

    # =================================================
    # POST
    # =================================================

    if request.method == "POST":

        title = request.form.get(
            "title",
            ""
        ).strip()

        image = request.files.get(
            "image"
        )

        # -----------------------------------------
        # Get old image
        # -----------------------------------------

        cur.execute("""
            SELECT image
            FROM gallery
            WHERE id=%s
        """, (id,))

        old_photo = cur.fetchone()

        if not old_photo:

            cur.close()

            flash(
                "Gallery image not found."
            )

            return redirect(
                "/gallery/manage"
            )

        old_image_url = old_photo[0]

        # -----------------------------------------
        # New image selected
        # -----------------------------------------

        if image and image.filename:

            try:

                # Upload new image
                result = cloudinary.uploader.upload(
                    image,
                    folder="brightfuture/gallery"
                )

                new_image_url = result.get(
                    "secure_url"
                )

                if not new_image_url:

                    cur.close()

                    flash(
                        "New image upload failed."
                    )

                    return redirect(
                        f"/gallery/edit/{id}"
                    )

                # ---------------------------------
                # Update database
                # ---------------------------------

                cur.execute("""
                    UPDATE gallery
                    SET title=%s, image=%s
                    WHERE id=%s
                """, (
                    title,
                    new_image_url,
                    id
                ))

                mysql.connection.commit()

                # ---------------------------------
                # Delete old Cloudinary image
                # ---------------------------------

                delete_cloudinary_image(
                    old_image_url
                )

                flash(
                    "Gallery image updated successfully!"
                )

            except Exception as e:

                mysql.connection.rollback()

                print(
                    "Cloudinary edit error:",
                    e
                )

                flash(
                    "Gallery update failed."
                )

        # -----------------------------------------
        # Only title changed
        # -----------------------------------------

        else:

            cur.execute("""
                UPDATE gallery
                SET title=%s
                WHERE id=%s
            """, (
                title,
                id
            ))

            mysql.connection.commit()

            flash(
                "Gallery title updated successfully!"
            )

        cur.close()

        return redirect(
            "/gallery/manage"
        )

    # =================================================
    # GET
    # =================================================

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
# DELETE CLOUDINARY IMAGE HELPER
# =====================================================

def delete_cloudinary_image(image_url):

    try:

        if not image_url:
            return

        # -----------------------------------------
        # Only process Cloudinary URLs
        # -----------------------------------------

        if "res.cloudinary.com" not in image_url:

            return

        # -----------------------------------------
        # Extract public_id
        #
        # Example:
        # .../upload/v123/brightfuture/gallery/abc.jpg
        #
        # Result:
        # brightfuture/gallery/abc
        # -----------------------------------------

        upload_part = image_url.split(
            "/upload/",
            1
        )[1]

        parts = upload_part.split("/")

        # Remove version if present
        if parts[0].startswith("v") and parts[0][1:].isdigit():

            parts = parts[1:]

        public_id_with_extension = "/".join(
            parts
        )

        # Remove file extension
        public_id = public_id_with_extension.rsplit(
            ".",
            1
        )[0]

        cloudinary.uploader.destroy(
            public_id,
            resource_type="image"
        )

    except Exception as e:

        print(
            "Cloudinary delete error:",
            e
        )


# =====================================================
# DELETE GALLERY IMAGE
# =====================================================

@gallery_bp.route(
    "/gallery/delete/<int:id>"
)
def gallery_delete(id):

    cur = mysql.connection.cursor()

    # -----------------------------------------
    # Get image URL
    # -----------------------------------------

    cur.execute("""
        SELECT image
        FROM gallery
        WHERE id=%s
    """, (id,))

    result = cur.fetchone()

    if not result:

        cur.close()

        flash(
            "Gallery image not found."
        )

        return redirect(
            "/gallery/manage"
        )

    image_url = result[0]

    try:

        # -----------------------------------------
        # Delete database record
        # -----------------------------------------

        cur.execute("""
            DELETE FROM gallery
            WHERE id=%s
        """, (id,))

        mysql.connection.commit()

        # -----------------------------------------
        # Delete image from Cloudinary
        # -----------------------------------------

        delete_cloudinary_image(
            image_url
        )

        flash(
            "Gallery image deleted successfully!"
        )

    except Exception as e:

        mysql.connection.rollback()

        print(
            "Gallery delete error:",
            e
        )

        flash(
            "Gallery image could not be deleted."
        )

    finally:

        cur.close()

    return redirect(
        "/gallery/manage"
    )