#Assignment 1
#soln 2
#Finding a person's income tax
print("Question 2")
x=int(input("Enter your Gross Income( in nearest penny)- $ ")) #input of gross income by user
y=int(input("Enter the number of Dependents- ")) #number of dependents
z=x-10000-(y*3000) #calculating tax income
t=z*0.2  #Total tax
print("Your tax is $",t)
