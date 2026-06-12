def fibo(a):
    dp=[0]*(a)
    dp[0]=0
    dp[1]=1 
    for i in range(2,a):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[a-1]

def prime(a):
    if a==1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

def readFile(fileName):
    with open(fileName,"r",encoding="utf-8") as file:
        content = file.read()
        return content

def writeFile(fileName):
    with open(fileName,"w",encoding="utf-8") as file:
        file.write("This the sample file.\n")
    print("Successfully written")
a=int(input())
print("Fibonacci of ",a," is ",fibo(a))
print(a," is a prime number ",prime(a))

print("File Write in process.....")
writeFile("sample.txt")
print("File Read in process.....")
print(readFile("sample.txt"))