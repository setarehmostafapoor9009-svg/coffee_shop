# Menu.py - مدیریت منوی کافه

# منوی کافه به صورت دیکشنری (نام محصول: قیمت به تومان)
menu = {
    "coffee": 80000,
    "tea": 50000,
    "cake": 120000,
}


def show_menu():
    """نمایش نام و قیمت محصولات کافه"""
    print("\n------------ Menu ------------")
    for name, price in menu.items():
        print(f"{name:<15} {price:>10,} Toman")
    print("------------------------------")
