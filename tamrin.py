#عددی را دریافت کرده و اعداد کوچک تر از ان را چاپ کند
#num = int(input("number vared kon"))

#for i in range(num):
    #print(i)

#عددی را دریافت کرده و مقسوم علیه های ان را چاپ کند
#num = int(input("number vared kon"))

#for i in range(1, num + 1):
    #if num % i == 0:
        #print(i)

#عددی را دریافت کرده و تشخیص دهد عدد اول است یا نه
#def is_prime(n):
    #if n <= 1 :
          #return False
    #for i in range(2 , n):
         #if n % i == 0:
              #return False
    #return True
#num = int(input("number vared kon"))

# is_prime(num):
    #print("adad aval ast")
#else:
    #print("adad aval nis")

#عددی را دریافت کرده و اعداد زوج کوچک تر از ان را چاپ کند
#number = int(input("number vared kon"))

#print(number)
#for i in range(0 , number):
    #if i % 2 == 0:
        #print(i)

#عددی را دریلافت کرده و اعداد اول کوچک تر از ان را چاپ کند
#number = int(input("number vared kon"))

#print(number)
#for i in range(2 , number):
    #is_prime = True
    #for j in range(2 , int(i ** 0.5) + 1):
        #if i % j == 0:
            #is_prime = False
            #break
    #if is_prime:
        #print(i)

#عددی رو دریافت کرده و اعداد زوج دورقمی کوچک تر از ان را چاپ کند
#number = int(input("number vared kon"))

#print(number)
#for i in range(10 , min(number , 100)):
    #if i % 2 == 0:
        #print(i)

#دو عدد رو دریافت کرده و مقسوم علیه مشترک ان هارا چاپ کند
#number1 = int(input("number vared kon"))
#number2 = int(input("number vared kon"))

#min_number = min(number1,number2)

#print(number1,number2)

#for i in range(1 , min_number + 1):
    #if number1 % i == 0 and number2 % i ==0:
        #print(i)

#دو عدد را دریافا کرده و با انتخاب خود کاربر اعداد زوج یا فرد بین دو عدد را چاپ کند
#number1 = int(input("number vared kon"))
#number2 = int(input("number vared kon"))
#choice = input("میخوای اعداد زوج رو ببینی یا فرد").strip().lower()

#start = min(number1 , number2)
#end = max(number1 , number2)

#print(f"اعداد{choice}بین{start}و{end} :عبارت اند از ")

#for i in range(start + 1, end):
    #if choice == "زوج" and  i % 2 == 0:
        #print(i)
    #elif choice == "فرد" and i % 2 != 0:
        #print(i)

#تعدادی عدد از کاربر دریافت کرده و بزرگترین و مجموع انها را چاپ کند (دقت کنیدمحدودیتی برای تعداد در نظر گرفته نشده و میتونید مثلا عدد 0 یا 01 رو پایان ورود اعداد دریافتی قرار دهید)
#numbers = []

#while True:
    #n = input(":عدد را وارد کنید(برای پایان 0 یا 01 را وارد کنید")

    #if n == "0" or n == "01":
        #break

    #try:
        #num = int(n)
        #numbers.append(num)
    #except ValueError:
        #print("لطفا فقط عدد صحیح وارد کنید")
#if len(numbers) == 0:
    #print("هیچ عددی وارد نشده")
#else:
    #print("bozorg tarin adad vared shode", max(numbers))
    #print("majmo adad vared shode", sum(numbers))

#عددی رو در مبنای ده دهی دریافت کرده و به مبنای دودویی تبدیل کند
#decimal = int(input(":یک عدد در مبنای دودویس وارد کنید"))

#binary = bin(decimal)[2:]
#print("(Binary):", binary)