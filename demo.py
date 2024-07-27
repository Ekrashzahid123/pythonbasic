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
#-------------------------String Method-------------------------------
#capatalize method 
name=f"my Name is  EKrash zahid and i am {age} year old" # type: ignore
x=name.capitalize()
print("Convert the string into capital form meanfirst letter is capital and rest of string is same",x)
#encode this is very useful as string
name5="My name is Ståle"
a=name5.encode()
print("The encode method work as",a)
#---------------------------LIST IN PYTHON----------------------------
#LIST=is collection of ordered and changeable.with dublicates member

mylist=["EKRASH ZAHID","USMAN NASIR","SUHBAN AMJAD"]
print("PRINTING MY FIRST LIST IN PYTHON",mylist)
#Finding the length of the list 
print("The length of the list is as",len(mylist))
#checking the type of the list
print("The type of the list is as",type(mylist))
#----------------ACCESSING THE TUPLE ------------------------------------
#we will use the same list as mylist
print("The index one of mylist is as",mylist[1])
print("The list range from",mylist[1:])
print("The list ranges from",mylist[1:3])
thistuple=["Apple","Mango","Hello world"]
if "Apple" in thistuple:
 print("YES APPLE IS PRESENT")
 #will be continue soon part of tuple not list
 #--------------------Change list item in python--------------------------
 mynewlist=["apple",'mango','Orange','kiwi','banana','Pineappple']
 print("Nor updated list is as",mynewlist)
 mynewlist[2]="Ekrash zahid"
 print("The updated list is as",mynewlist)
 mynewlist[1:4]=["ali",'Usman']
 print("The udated list once again is as",mynewlist)
 #-------------insert method in python-----------------------------------
 mylist1=['Ali',"Hamza","usman"]
 print("NOt UPDATED LIST IS AS",mylist1)
 mylist1.insert(1,"GOOD")
 print("UPDATED LIST IS AS",mylist1)
 #---------------------ADD LIST PYTHON------------------------------------
 mylist2=["ali",'Me','You']
 add=['I','Me','You']
 mylist2.append("a")
 print("list with append is as",mylist2)
 mylist2.extend(add)
 print("list with extend",mylist2)
 #-------------------REMOVE IN THE LIST --------------------------------
 mylist4=["i",'Love',"python"]
 print("The list is as",mylist4)
 mylist4.remove("i"); # type: ignore
print("The list after remove of element is as",mylist4)
mylist4.pop(1)
print("the list after pop of 2 indec is as",mylist4)
mylist4.insert(0,"i")
mylist4.insert(1,'Love')
#WE WILL CONTINUE FROM LOOP LIST
mylist6=["Orange","Object oriented","Apple"]
print("USing for loop and print the element in the list")
for c in mylist6:
 print(c)
 #using while loop to print the list
 i = 0
while i < len(mylist6):
    print(mylist6[i])
    i = i + 1  # increment statement should be indented
#---------------------LIST COMPREHESION------------------------------
mylist2=["EKrash","USMAN","KIWI","AMROOD"]
newlist=[]
for x in mylist2:
  if "K"in x:
    newlist.append(x)

    print(newlist)
# THIS IS THE WAY WE CAN TAKE OUT OUR DESIRING VALUE
#----------------------SORTING THE LIST------------------------------
mysorting=[90,21,43,222,789]
mysorting.sort(reverse=True)
print("THE DESCENDING SORTING IS AS",mysorting)
#-----------------ASECINDING SORTING IS AS------------------------
mysorting=[90,87,55,44,31,00]
mysorting.sort()
print("THE ASCENDING SORTING IS AS",mysorting)
#-----------COPY LIST-------------------------------------------
my=[1,2,4,5,6,7]
list0=my.copy()
print("THE NEW LIST IS AS COPY FUNCTIONALITY",list)





 









