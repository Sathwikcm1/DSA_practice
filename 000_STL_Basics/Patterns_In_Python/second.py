#FIXME: this is the second pattern given in striver A-Z sheet.

no = int(input("Enter the size for pattern: "))
for i in range(no,0,-1):
    print("* " * (i))

#NOTE: this will print the ulta triangle , 
#note: the python for loop , in range function we have got three parameters, range(start,end, step)
#start represents where the loop starts from, by default it is zero.
#end represents where the loop ends, and it is excluding the end(no)
#step, if negative it will count backwords, otherwise it will go from start.

