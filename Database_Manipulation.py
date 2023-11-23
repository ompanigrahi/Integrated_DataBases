print()
a=("Car Showroom Management")
print(a.center(120," "))
b=("Developed by Om & Jay")
print(b.center(228," "))
c=("=====================")
print(c.center(120," "))
d=("This is a PASSWORD PROTECTED Programme")
print(d.center(120," "))
pw=("ADMIN@0000")
for i in range(3):
    if i==0:
        password=str(input("Enter The Password:"))
    if i==1:
        password=str(input("Enter The Password(2 attempts left):"))
    if i==2:
        password=str(input("Enter The Password(1 attempt left):"))
    if password==pw:
        print()
        print("============================================================================================================================")
        print()

        add=("Add Entry = add")
        print(add.center(120," "))

        delete=("Delete Entry = delete")
        print(delete.center(120," "))

        stocks=("View Total Stocks = view")
        print(stocks.center(120," "))
    
        modify=("To Modify = modify")
        print(modify.center(120," "))
    
        search=("To Search = search")
        print(search.center(120," "))
    
        information=("TO View The Information = info")
        print(information.center(120," "))

        clear=("TO Delete The Database = clear")
        print(clear.center(120," "))

        Exit=("To Exit The Program = quit")
        print(Exit.center(120," "))
    
        gap=("=====================")
        print(gap.center(120," "))
    


        def add():
            print("Add in the format of (Model No.,'Car Name','Colour','No. Of Pieces Available')")
            a=str(input("Enter a list"))
            fh=open("D:\\#OP67\\codename ()\\abcdef.txt",'a',newline='')
            fh.write(a)
            fh.write("\n")
            fh.close()
            input("Press any key to move forward")



        def stockyard():
            fh=open("D:\\#OP67\\codename ()\\abcdef.txt",'r')
            z=fh.readlines()
            for i in z:
                print(i)
            fh.close()
            input("Press any key to move forward")



        def search():
            z=int(input("Enter the car to view its stock in the stockyard;"))
            fh=open("D:\\#OP67\\codename ()\\abcdef.txt",'r')
            x=fh.readlines()
            b=x.pop(z)
            print(b)
            fh.close()
            input("Press any key to move forward")



        def delete():
            y=int(input("Enter the last digit of the model no."))
            fh=open("D:\\#OP67\\codename ()\\abcdef.txt",'r')
            z=fh.readlines()
            z.pop(y)
            fh.close()
            fh=open("D:\\#OP67\\codename ()\\abcdef.txt",'w')
            for i in z:
                fh.write(i)
    
            fh.close()
            input("Press any key to move forward")



        def modify():
            y=int(input("Enter the last digit of the model no."))
            q=str(input("Enter the modified record."))
            fh=open("D:\\#OP67\\codename ()\\abcdef.txt",'r')
            z=fh.readlines()
            z.pop(y)
            fh.close()
            fh=open("D:\\#OP67\\codename ()\\abcdef.txt",'w')
            for i in range(y):
                fh.write(z[i])
            fh.close()
            fh=open("D:\\#OP67\\codename ()\\abcdef.txt",'a',newline='')
    
            fh.write(q)
            fh.write('\n')
            fh.close()
            fh=open("D:\\#OP67\\codename ()\\abcdef.txt",'a')
            for i in range(y,35):
                fh.write(z[i])
            fh.close()
            input("Press any key to move forward")

        def info():
            x=input("To get the info enter the car name:_")
            a=x.lower()
            if a=='tiago':
                print("Price Range ----------> ₹5.44lakh ---> ₹7.90lakh","\n","ARAI Mileage ----------> 26.49km/kg","\n","City Mileage ----------> 23.0km/kg","\n","Secondary Fuel Type ----------> Petrol","\n","Fuel type ----------> CNG","\n","Engine Displacement(cc) ----------> 1199","\n","No. of Cylinder ----------> 3","\n","Max Power(bhp@rpm) ----------> 72bhp@6000rpm","\n","Max Torque(nm@rpm) ----------> 95nm@3500rpm","\n","Seating Capacity ----------> 5","\n","Transmission Type ----------> Manual","\n","Fuel Tank Capacity ----------> 60.0","\n","Body Type ----------> Hatchback","\n","Ground clearance Unladen ----------> 168")
                input("Press any key to move forward")
            if a=='tigor':
                print("Price Range ----------> ₹6.10lakh ---> ₹8.84lakh","\n","ARAI Mileage ----------> 26.49km/kg","\n","City Mileage ----------> 26.93km/kg","\n","Boot Space (Litres) ----------> 205","\n","Fuel type ----------> CNG","\n","Engine Displacement(cc) ----------> 1199","\n","No. of Cylinder ----------> 3","\n","Max Power(bhp@rpm) ----------> 72.40bhp@6000rpm","\n","Max Torque(nm@rpm) ----------> 95nm@3500rpm","\n","Seating Capacity ----------> 5","\n","Transmission Type ----------> Manual","\n","Fuel Tank Capacity ----------> 60.0","\n","Body Type ----------> Sedan","\n","Ground clearance Unladen ----------> 170")
                input("Press any key to move forward")
            if a=='punch':
                print("Price Range ----------> ₹6.00lakh ---> ₹9.54lakh","\n","ARAI Mileage ----------> 18.82km/kg","\n","City Mileage ----------> 14.42km/kg","\n","Boot Space (Litres) ----------> 366","\n","Fuel type ----------> PETROL","\n","Engine Displacement(cc) ----------> 1199","\n","No. of Cylinder ----------> 3","\n","Max Power(bhp@rpm) ----------> 84.48bhp@6000rpm","\n","Max Torque(nm@rpm) ----------> 113nm@3300+/-rpm","\n","Seating Capacity ----------> 5","\n","Transmission Type ----------> Automatic","\n","Fuel Tank Capacity ----------> 37.0","\n","Body Type ----------> SUV","\n","Ground clearance Unladen ----------> 187")
                input("Press any key to move forward")
            if a=='nexon':
                print("Price Range ----------> ₹7.70lakh ---> ₹14.18 lakh","\n","ARAI Mileage ----------> 22.07 kmpl","\n","City Mileage ----------> 18.5 kmpl","\n","Body Type ----------> SUV","\n","Fuel type ----------> Diesel","\n","Engine Displacement(cc) ----------> 1497","\n","No. of Cylinder ----------> 4","\n","Max Power(bhp@rpm) ----------> 108.67bhp@4000rpm","\n","Max Torque(nm@rpm) ----------> 260nm@1500-2750rpm","\n","Seating Capacity ----------> 5","\n","Transmission Type ----------> Automatic","\n","Fuel Tank Capacity ----------> 44.0","\n","Boot Space ----------> 350","\n","Ground clearance Unladen ----------> 210")
                input("Press any key to move forward")
            if a=='harrier':
                print("Price Range ----------> ₹14.80lakh ---> ₹22.25 lakh","\n","ARAI Mileage ----------> 14.6 kmpl","\n","City Mileage ----------> 11.50 kmpl","\n","Body Type ----------> SUV","\n","Fuel type ----------> Diesel","\n","Engine Displacement(cc) ----------> 1956","\n","No. of Cylinder ----------> 4","\n","Max Power(bhp@rpm) ----------> 167.67bhp@3750rpm","\n","Max Torque(nm@rpm) ----------> 350nm@1750-2000rpm","\n","Seating Capacity ----------> 5","\n","Transmission Type ----------> Automatic","\n","Fuel Tank Capacity ----------> 50.0","\n","Boot Space ----------> 425","\n","Ground clearance Unladen ----------> 205")
                input("Press any key to move forward")
            if a=='safari':
                print("Price Range ----------> ₹15.45lakh ---> ₹23.76 lakh","\n","ARAI Mileage ----------> 14.08 kmpl","\n","City Mileage ----------> 14.0 kmpl","\n","Body Type ----------> SUV","\n","Fuel type ----------> Diesel","\n","Engine Displacement(cc) ----------> 1956","\n","No. of Cylinder ----------> 4","\n","Max Power(bhp@rpm) ----------> 167.67bhp@3750rpm","\n","Max Torque(nm@rpm) ----------> 350nm@1750-2000rpm","\n","Seating Capacity ----------> 6,7","\n","Transmission Type ----------> Automatic","\n","Fuel Tank Capacity ----------> 50.0","\n","Boot Space ----------> 73","\n","Ground clearance Unladen ----------> 205")
                input("Press any key to move forward")
    
        def clear():
            fh=open("D:\\#OP67\\codename ()\\abcdef.txt",'w')
            fh.write()
            fh.close()
        while True:
            a = input('Enter the Function:_ ')
            if a == 'add':
                add()
            if a == 'search':
                search()
            if a == 'view':
                stockyard()
            if a == 'delete':
                delete()
            if a == 'modify':
                modify()
            if a == 'info':
                info()
            if a == 'clear':
                clear()
            if a == 'quit':
                print("You have chosen to quit the program.." )
                break
            else:
                print("Enter the next function")
    else:
        print("Wrong Password")
print("You Have Exceeded The Password Limit")




