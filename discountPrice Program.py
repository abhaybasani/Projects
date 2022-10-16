# -------------------------------Discount calculation program--------------------------
class Discount:
    def dis(self):
        try:
            # ------------------give user a discount program--------------
            price = int(input("enter price of product"))
            discount = int(input("enter how much you won't discount"))
            a = price * discount / 100
            tp = price - a
            print("your discount is:", a)
            print("after discount price is:", tp)
        except ValueError:
            print("##please enter int type value! next time")
        except KeyboardInterrupt:
            print("program is finish. Thanks you.")
DiscountPgm=Discount()
DiscountPgm.dis()