m1=float(input("Enter marks of subject 1 :"))
m2=float(input("Enter marks of subject 2 :"))
m3=float(input("Enter marks of subject 3 :"))

total=m1+m2+m3
average=total/3

print("=======FINAL SCORECARD=======")
print("Subject 1:",m1)
print("Subject 2:",m2)
print("Subject 3:",m3)
print("Total Marks:",total)
print("Average:",round(average,2))