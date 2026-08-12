from flask import Blueprint, render_template, request
from config import mysql


analytics_bp = Blueprint("analytics", __name__)


# =========================
# RECORD PAGE VIEW
# =========================

def record_view(page_name):

    cur = mysql.connection.cursor()

    cur.execute(
        """
        INSERT INTO analytics
        (page_name, element_name, event_type)
        VALUES (%s, %s, %s)
        """,
        (page_name, None, "view")
    )

    mysql.connection.commit()
    cur.close()


# =========================
# RECORD ELEMENT CLICK
# =========================

def record_click(page_name, element_name):

    cur = mysql.connection.cursor()

    cur.execute(
        """
        INSERT INTO analytics
        (page_name, element_name, event_type)
        VALUES (%s, %s, %s)
        """,
        (page_name, element_name, "click")
    )

    mysql.connection.commit()
    cur.close()


# =========================
# CLICK API
# =========================

@analytics_bp.route("/analytics/click", methods=["POST"])
def analytics_click():

    data = request.get_json()

    page_name = data.get("page_name")
    element_name = data.get("element_name")

    record_click(page_name, element_name)

    return {"success": True}


# =========================
# ANALYTICS DASHBOARD
# =========================

@analytics_bp.route("/analytics-dashboard")
def analytics_dashboard():

    cur = mysql.connection.cursor()

    # -------------------------
    # TODAY VIEWS
    # -------------------------

    cur.execute("""
        SELECT COUNT(*)
        FROM analytics
        WHERE event_type = 'view'
        AND DATE(created_at) = CURDATE()
    """)

    today = cur.fetchone()[0]


    # -------------------------
    # WEEK VIEWS
    # -------------------------

    cur.execute("""
        SELECT COUNT(*)
        FROM analytics
        WHERE event_type = 'view'
        AND YEARWEEK(created_at, 1)
        = YEARWEEK(CURDATE(), 1)
    """)

    week = cur.fetchone()[0]


    # -------------------------
    # MONTH VIEWS
    # -------------------------

    cur.execute("""
        SELECT COUNT(*)
        FROM analytics
        WHERE event_type = 'view'
        AND YEAR(created_at) = YEAR(CURDATE())
        AND MONTH(created_at) = MONTH(CURDATE())
    """)

    month = cur.fetchone()[0]


    # -------------------------
    # YEAR VIEWS
    # -------------------------

    cur.execute("""
        SELECT COUNT(*)
        FROM analytics
        WHERE event_type = 'view'
        AND YEAR(created_at) = YEAR(CURDATE())
    """)

    year = cur.fetchone()[0]


    # -------------------------
    # PAGE VIEWS
    # -------------------------

    cur.execute("""
        SELECT page_name, COUNT(*) AS total
        FROM analytics
        WHERE event_type = 'view'
        GROUP BY page_name
        ORDER BY total DESC
    """)

    page_views = cur.fetchall()


    # -------------------------
    # ALL ELEMENT CLICKS
    # -------------------------

    cur.execute("""
        SELECT
            page_name,
            element_name,
            COUNT(*) AS total
        FROM analytics
        WHERE event_type = 'click'
        GROUP BY page_name, element_name
        ORDER BY total DESC
    """)

    click_data = cur.fetchall()


    # -------------------------
    # TODAY CLICKS
    # -------------------------

    cur.execute("""
        SELECT element_name, COUNT(*) AS total
        FROM analytics
        WHERE event_type = 'click'
        AND DATE(created_at) = CURDATE()
        GROUP BY element_name
        ORDER BY total DESC
    """)

    today_clicks = cur.fetchall()


    # -------------------------
    # WEEK CLICKS
    # -------------------------

    cur.execute("""
        SELECT element_name, COUNT(*) AS total
        FROM analytics
        WHERE event_type = 'click'
        AND YEARWEEK(created_at, 1)
        = YEARWEEK(CURDATE(), 1)
        GROUP BY element_name
        ORDER BY total DESC
    """)

    week_clicks = cur.fetchall()


    # -------------------------
    # MONTH CLICKS
    # -------------------------

    cur.execute("""
        SELECT element_name, COUNT(*) AS total
        FROM analytics
        WHERE event_type = 'click'
        AND YEAR(created_at) = YEAR(CURDATE())
        AND MONTH(created_at) = MONTH(CURDATE())
        GROUP BY element_name
        ORDER BY total DESC
    """)

    month_clicks = cur.fetchall()


    # -------------------------
    # YEAR CLICKS
    # -------------------------

    cur.execute("""
        SELECT element_name, COUNT(*) AS total
        FROM analytics
        WHERE event_type = 'click'
        AND YEAR(created_at) = YEAR(CURDATE())
        GROUP BY element_name
        ORDER BY total DESC
    """)

    year_clicks = cur.fetchall()


    cur.close()


    return render_template(
        "analytics_dashboard.html",

        today=today,
        week=week,
        month=month,
        year=year,

        page_views=page_views,
        click_data=click_data,

        today_clicks=today_clicks,
        week_clicks=week_clicks,
        month_clicks=month_clicks,
        year_clicks=year_clicks
    )