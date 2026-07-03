import matplotlib.pyplot as plt

def create_graphs(monthly_sales, product_sales, city_sales):

    # Monthly Sales Bar Chart
    plt.figure(figsize=(10,5))
    plt.bar(monthly_sales.index, monthly_sales.values)
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("monthly_sales.png")
    plt.close()


    # Product Sales Bar Chart
    plt.figure(figsize=(12,5))
    plt.bar(product_sales.index, product_sales.values)
    plt.title("Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("product_sales.png")
    plt.close()


    # City Sales Pie Chart
    plt.figure(figsize=(8,8))
    plt.pie(city_sales.values,
            labels=city_sales.index,
            autopct="%1.1f%%")
    plt.title("Sales by City")
    plt.tight_layout()
    plt.savefig("city_sales.png")
    plt.close()
