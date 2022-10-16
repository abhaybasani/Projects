class HM_Calc:
    def calc(self):
        try:
            while (1):
                print("calculator peramiterize")

                def cal(num1, opr, num2):
                    print("Ques: ", num1, opr, num2)

                num1 = int(input("enter your first number: "))
                opr = input("enter your operation b/w= ( + , - , * , / ) for exit=0:")
                num2 = int(input("enter your second number: "))
                if opr and num1 == 0:
                    exit()
                if opr == '+':
                    print("Result: ", num1 + num2)
                elif opr == '-':
                    print("Result: ", num1 - num2)
                elif opr == '*':
                    print("Result: ", num1 * num2)
                elif opr == '/':
                    print("Result: ", num1 / num2)
                else:
                    print("Invaild")
                cal(num1, opr, num2)
        except ValueError:
            print("##please enter int type value! next time")
        except KeyboardInterrupt:
            print("program is finish. Thanks you.")
cal=HM_Calc()
cal.calc()