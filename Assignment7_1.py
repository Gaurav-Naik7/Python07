def pattern(no):
    if(no>0):
        print("*",end=" ")
        no=no-1
        pattern(no)

def main():
    x=int(input("Enter number of stars: "))
    pattern(x)

if __name__=="__main__":
    main()
