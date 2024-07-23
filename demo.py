import random as ran
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
name=['Ali',"hamza","usman"] # type: ignore
name_1,name_2,name_3=name # type: ignore
print("Name_1 is as",name_1)
print("Name_2 is as",name_2)
print("Name_3 is as",name_3)
#Noted in python if we combine the int and string it will not be executed 
#------------------------CONCEPT OF GLOBAL VARIABLE---------------------#
#GLOBAL VARIABLE = create variable outside the function and use it inside the function
x = "good"

def myfun():
    print("Python is " + x) # type: ignore

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
#-----------------------Data Type---------------------------------------------------------\
#have a look on w3 school

#-----------------------PYTHON NUMBER_-------------------------------------
#Threee types 1 int 2 float 3 comples

no1=1   #int
no2=3.44 #float
no3=2j    #complex

#prinitng the typw in python for the conformation
print("The Type of no1 is as:",type(no1))
print("The Type of no2 is as:",type(no2))
print("The Type of no3 is as",type(no3))

#Conversion of the type to type

a=float(no1)  #converting the int into float
b=int(no2)   #converting the complex into int
c=complex(no3) #converting the float into complex

# printing the following conversion

print("The conversion from int to float is as",a)
print("The conversion from complex into int is as",b)
print("The conversion from float into complex is as",c)
#-------------------------MODULE RANDOM IN PYTHON USED TO GENERATE RANDOM NUMBER_-------------------------------
print("GENERATING THE RANDOM NUMBER ")
print("The random number is as",ran.randrange(1,9))
#-------------------------PYTHON CASTING-------------------------------------------------------------------------
a=1
b=2.1
c="5"
print("The casting is as",int(a))
print("The casting is as",int(b))
print("The casting is as",int(c))

#same as complex and float

#------------------------PYTHON STRING----------------------------------------------------
x="Ekrash zahid"
print(x[:2])  #returing staring 2 element
print(x[2:])  #returning all the element ignoring first 2
print(x[2:5]) #output ras

#--------------------Upper case string------------------------------------
x="ahmed"
a="USMAN"
print("Converting all the cases to upper is as",x.upper())
print("Converting all the cases to lower case",a.lower())

#strip removes the space in end and at start
p=" ham or ap "
print("the output is as",p.strip())
h='Jkrash Zahid'   #correcting the name
print("Replace method is as",h.replace("J",'E'))
#---------------------Formatting string----------------------------
age=21;
#name4="my name is ekrash and i am age old "  #this will throw an error
name4=f"my name is ekrash and i am {age} years old "  #correct way to formatting the string
print(name4) 
length =2
breath =1
area=f"the area of square is equal to {length+breath}"
print(area)




