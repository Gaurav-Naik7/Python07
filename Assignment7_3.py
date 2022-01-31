def pattern(no):
    if(no>0):
        print(no,end=" ")
        no=no-1
        pattern(no)

def main():
    x=int(input("Enter a number: "))
    pattern(x)

if __name__=="__main__":
    main()
