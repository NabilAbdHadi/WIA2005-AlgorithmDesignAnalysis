#Create a program, print out all even numbers between 1-­‐100.
# Calculate time  complexity of the program.

for i in range(1,101):
    if(i%2==0):
        print(i,end=", ")
    if(i%40==0):
        print("");
