# Main.py - اجرای برنامه اصلی
from Menu import show_menu
from Order import add_order, show_orders
from Billing import calculate_total, print_invoice


def main():
    while True:
        print("\n========== Coffee Shop ==========")
        print("1. نمایش منوی کافه")
        print("2. ثبت سفارش")
        print("3. نمایش سفارش‌ها")
        print("4. محاسبه مبلغ کل")
        print("5. چاپ فاکتور")
        print("6. خروج")
        choice = input("انتخاب شما: ").strip()

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_order()
        elif choice == "3":
            show_orders()
        elif choice == "4":
            print(f"مبلغ کل: {calculate_total():,} Toman")
        elif choice == "5":
            print_invoice()
        elif choice == "6":
            print("خداحافظ!")
            break
        else:
            print("گزینه نامعتبر است. یک عدد از 1 تا 6 وارد کنید.")


main()
