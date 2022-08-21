height=int(input("Height :"))

for i in range(height+1):
    print(" "*(height-i),end="")
    print("#"*i,end="")
    print("  ",end="")
    print("#"*i)
    
    