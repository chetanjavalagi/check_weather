degree=int(input("enter the Degree: "))
if degree <=20:
    print("clod weather")
elif degree >20 and degree <=38:
    print("normal weather")
else :
    print("hot! weather")
fahrenheit=((degree*1.8)+32)
print("The Fahrenheit value is ",fahrenheit,"F")