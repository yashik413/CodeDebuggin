Input = [] 
ans = -1				#Initialised ans to -1
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    Input.append(ele)
if(Input[0]<0):
    prev =1
else:
    prev=-1
for elem in Input:
        if elem ==0: 			# Equal sign Added
                sign = 1		# Changed sign = -1 to sign = 1
        else: 
                sign = elem / abs(elem)

        if sign == -prev: 
                ans = ans + 1
                prev = sign
print(ans)				#To print the output
