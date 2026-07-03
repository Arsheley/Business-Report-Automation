from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def create_pdf(
        total_sales,
        total_orders,
        average_sale,
        best_product,
        best_city,
        best_month,
        monthly_sales,
        product_sales,
        city_sales):

    doc = SimpleDocTemplate("Business_Report.pdf")

    styles = getSampleStyleSheet()

    elements = []

    # ===============================
    # Title
    # ===============================
    elements.append(
        Paragraph("Business Sales Analysis Report", styles["Title"])
    )

    elements.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d %B %Y   %I:%M %p')}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 20))
    elements.append(Paragraph("<hr/>", styles["Normal"]))
    elements.append(Spacer(1, 15))

    # ===============================
    # Business Summary
    # ===============================
    elements.append(
        Paragraph("Business Summary", styles["Heading1"])
    )

    elements.append(
        Paragraph(f"<b>Total Sales:</b> ${total_sales:,.2f}", styles["Normal"])
    )

    elements.append(
        Paragraph(f"<b>Total Orders:</b> {total_orders}", styles["Normal"])
    )

    elements.append(
        Paragraph(f"<b>Average Sale:</b> ${average_sale:,.2f}", styles["Normal"])
    )

    elements.append(
        Paragraph(f"<b>Best Selling Product:</b> {best_product}", styles["Normal"])
    )

    elements.append(
        Paragraph(f"<b>Best Performing City:</b> {best_city}", styles["Normal"])
    )

    elements.append(
        Paragraph(f"<b>Best Performing Month:</b> {best_month}", styles["Normal"])
    )

    elements.append(Spacer(1, 20))
    elements.append(Paragraph("<hr/>", styles["Normal"]))
    elements.append(Spacer(1, 15))

    # ===============================
    # Monthly Sales Graph
    # ===============================
    elements.append(
        Paragraph("Monthly Sales", styles["Heading2"])
    )

    elements.append(
        Image("monthly_sales.png", width=450, height=250)
    )

    elements.append(Spacer(1, 20))
    elements.append(Paragraph("<hr/>", styles["Normal"]))
    elements.append(Spacer(1, 15))

    # ===============================
    # Product Sales Graph
    # ===============================
    elements.append(
        Paragraph("Product Sales", styles["Heading2"])
    )

    elements.append(
        Image("product_sales.png", width=450, height=250)
    )

    elements.append(Spacer(1, 20))
    elements.append(Paragraph("<hr/>", styles["Normal"]))
    elements.append(Spacer(1, 15))

    # ===============================
    # City Sales Graph
    # ===============================
    elements.append(
        Paragraph("City Sales", styles["Heading2"])
    )

    elements.append(
        Image("city_sales.png", width=450, height=250)
    )

    elements.append(Spacer(1, 25))
    elements.append(Paragraph("<hr/>", styles["Normal"]))
    elements.append(Spacer(1, 15))

    # ===============================
    # End of Report
    # ===============================
    elements.append(
        Paragraph("End of Report", styles["Heading2"])
    )

    elements.append(Spacer(1, 10))

    elements.append(
        Paragraph(
            "This report was generated automatically using the Python Business Report Automation system.",
            styles["Italic"]
        )
    )

    doc.build(elements)