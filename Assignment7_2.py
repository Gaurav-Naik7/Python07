i=1
def pattern(no):
    global i
    if(i<=no):
        print(i,end=" ")
        i=i+1
        pattern(no)

def main():
    x=int(input("Enter a number: "))
    pattern(x)

if __name__=="__main__":
    main()
