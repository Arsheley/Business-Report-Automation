import split_data
import read_reports
import sales_report
import graphs
import pdf
import email_report
import logger
try:
    combined_data = read_reports.read_reports()

    (
        total_sales,
        total_orders,
        average_sale,
        best_product,
        best_city,
        best_month,
        monthly_sales,
        product_sales,
        city_sales
    ) = sales_report.create_sales_report(combined_data)
    graphs.create_graphs(monthly_sales, product_sales, city_sales)
    pdf.create_pdf(
        total_sales,
        total_orders,
        average_sale,
        best_product,
        best_city,
        best_month,
        monthly_sales,
        product_sales,
        city_sales
    )
    email_report.send_email(
        "MY_EMAIL@gmail.com",
        "MY_APP_PASSWORD",
        "RECIPIENT_EMAIL@gmail.com"
    )



    print("Business report generated successfully!")
except Exception as e:
    logger.log_run(f'FAILED-{e}')
    print(e)