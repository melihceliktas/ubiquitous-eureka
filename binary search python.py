c = []
a = []

b = input("Enter your numbers with backspaces =")            
c = b.split(" ")

for i in range(len(c)):
    try:
        a.append(int(c[i]))
    except:
        pass

a.sort()


size = len(a)


while True:
    while True:
        try:
            sayı = int(input("Enter a number to search="))
            break
        except:
            print("ENTER A NUMBER PLEASE!") 
    

    if sayı > a[int(size/2)] and sayı in a:
        for i in range(int(size/2),size):
            if sayı == a[i]:
                print(f"{a.index(sayı)+1}.")
                
                break
            



    elif sayı < a[int(size/2)] and sayı in a:
        for i in range(int(size/2)):
            if sayı == a[i]:
                print(f"{a.index(sayı)+1}.")
                break

    elif sayı == a[int(size/2)]:
        print(f"{a.index(sayı)}.")
        

    else:
        print("Number has not found.")
    
    

    x = input("Do you want to another process? y-n ")
        
    if x == "n":
        break


print("Have a good day!")



##Melih Çeliktaş
