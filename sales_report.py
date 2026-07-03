def create_sales_report(combined_data):

    total_sales = combined_data["Sales"].sum()
    total_orders = len(combined_data)
    average_sale = combined_data["Sales"].mean()

    best_product = combined_data.groupby("Product")["Quantity Ordered"].sum().idxmax()
    best_city = combined_data.groupby("City")["Sales"].sum().idxmax()
    best_month = combined_data.groupby("Month Name")["Sales"].sum().idxmax()

    monthly_sales = combined_data.groupby("Month Name")["Sales"].sum()

    product_sales = combined_data.groupby("Product")["Sales"].sum()

    city_sales = combined_data.groupby("City")["Sales"].sum()

    #print(f"Total Sales: ${total_sales:.2f}")
    #print(f"Total Orders: {total_orders}")
    #print(f"Average Sale: ${average_sale:.2f}")
    #print(f"Best Product: {best_product}")
    #print(f"Best City: {best_city}")
    #print(f"Best Month: {best_month}")

    return  (
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