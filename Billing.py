# Billing.py - محاسبه هزینه و صدور فاکتور
from Order import orders


def calculate_total():
    """مجموع قیمت × تعداد تمام سفارش‌ها را برمی‌گرداند"""
    total = 0
    for order in orders:
        total += order["price"] * order["count"]
    return total


def calculate_discount(total):
    """اگر مبلغ بیشتر از یک میلیون تومان باشد، ۱۰ درصد تخفیف برمی‌گرداند"""
    if total > 1000000:
        return total * 10 / 100
    return 0


def print_invoice():
    """چاپ فاکتور نهایی"""
    if len(orders) == 0:
        print("سفارشی ثبت نشده است؛ فاکتوری برای چاپ وجود ندارد.")
        return

    total = calculate_total()
    discount = calculate_discount(total)
    final_amount = total - discount

    print("\n============ Invoice ============")
    for order in orders:
        print(f"{order['name']:<12} x {order['count']:<4} = {order['price'] * order['count']:>12,.0f}")
    print("---------------------------------")
    print(f"مبلغ کل:          {total:,.0f} Toman")
    print(f"تخفیف:            {discount:,.0f} Toman")
    print(f"مبلغ نهایی:       {final_amount:,.0f} Toman")
    print("=================================")
