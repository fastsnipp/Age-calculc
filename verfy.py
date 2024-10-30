a=input("Enter Your Year Of Birth ")
a=int(a)
b=input("Enter Your Month Of birth ")
b=int(b)
year=(2024-a)
year=int(year)
month=(11-b)
month=int(month)
get_age=print("You Are ",year,"and",month,"months","old")

if(year>17):
    {
print("Congrats!! Your Age is ", year,"You are an Adult!!")
}

elif(year<18):
    { 
print("Hello Boy !! Your age is ", year , "You are not adult")
}
if(b>12):{
    print("invalid month Entered !! The outcome result may be defected")
}