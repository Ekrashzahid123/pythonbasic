print("Python first program")
#Python identation --giving space in the begining of the code
if 5>2:
 print("Five is greater then Two")
#declearing the variable 
x=5
y="Ekrash zahid"
#Comment in python
#THIS IS COMMENT
#MULTILINE COMMENT
#Creating variable 
x=4   #this is the int
y="HAMZA ZAHID"  #this is the str
print(x)
print(y)
#casting --used to specify the type of variable
k=int(3)
r=float(3)
s=str(3)
print(k)
print(r)
print(s) #here the variable type is specified
#getting the type of the variable 
print("The Type of k is as",type(k))
print("The type of r is as",type(r))
#string varaible can be declear using single or double quote
a="Ali"
m='ali'
print("The name with double quote",a)
print("The name with single quote",m)
#Case sensitive
a=6
A=0
print("The case sensitive with small letter",a)
print("The case sensitive with capital letter",A)
#Variable Name
#myvar _my_var mYVAR myVar legal variable names
#Illegal variable name
#0A ,& something like that
#case we will use snake case in our journey of programming my_var_test
#--------------Assigned multiple values-------------------------#
x,y,z= "orange","banana","Apple"
print("ASSIGNED MULTIPLE VALUE TO MULTIPLE VARIABLE")
print("The value of x is as",x)
print("The value of y is as",y)
print("The value of z is as",z)
#---------------One value to multiple variable-------------------#
print("ASSIGNED ONE VALUE TO MULTIPLE VARIABLE")
x=y=z="Orange"
print("The value of x is as",x)
print("The value of y is as",y)
print("The value of z is as",z)
#----------UNPACKING CONCEPT IN PYTHON-----------------------#
name=['Ali',"hamza","usman"]
name_1,name_2,name_3=name
print("Name_1 is as",name_1)
print("Name_2 is as",name_2)
print("Name_3 is as",name_3)
#Noted in python if we combine the int and string it will not be executed 
#------------------------CONCEPT OF GLOBAL VARIABLE---------------------#
#GLOBAL VARIABLE = create variable outside the function and use it inside the function
x = "good"

def myfun():
    print("Python is " + x)

print("Calling the function:")
myfun()

#checking local and global variable in python--------------------------------------
name_1="Ekrash"

def name():
   name_1="ALi"
   print("Working as local variable beacuse inside fun")
   print("My complete name is "+name_1)

print("CAlling the function")
name()

print("Working as global variale beacause outside the fun")
print("My complete name is "+name_1)
 