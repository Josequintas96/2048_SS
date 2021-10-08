import sys

print("Hello")
x=95
print(x)
print("Number of arguments: ", len(sys.argv) )
print("Argument List: ", str(sys.argv))
i =1
while i < len(sys.argv):
	print(sys.argv[i])
	i+=1

