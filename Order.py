# Order.py - مدیریت سفارش‌ها
from Menu import menu

# لیست سفارش‌ها؛ هر سفارش یک دیکشنری است
orders = []


def add_order():
    """دریافت نام محصول و تعداد از کاربر و ذخیره سفارش در لیست"""
    name = input("نام محصول: ").strip().lower()

    if name not in menu:
        print("این محصول در منوی کافه وجود ندارد.")
        return

    count_text = input("تعداد: ").strip()
    if not count_text.isdigit() or int(count_text) <= 0:
        print("تعداد باید یک عدد صحیح مثبت باشد.")
        return

    count = int(count_text)
    orders.append({
        "name": name,
        "price": menu[name],
        "count": count,
    })
    print(f"{count} عدد {name} به سفارش‌ها اضافه شد.")


def show_orders():
    """نمایش تمام سفارش‌های ثبت‌شده"""
    if len(orders) == 0:
        print("هنوز سفارشی ثبت نشده است.")
        return

    print("\n---------- Orders ----------")
    for number, order in enumerate(orders, start=1):
        print(f"{number}. {order['name']} | قیمت: {order['price']:,} | تعداد: {order['count']}")
    print("----------------------------")
