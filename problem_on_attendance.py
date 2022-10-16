total_no_of_classes=int(input("enter the number of classes:"))
days_attended=int(input("enter the total days you have attended:"))
attendance_required= (days_attended/total_no_of_classes)*100
if attendance_required>=75:
    print("your eligible:",attendance_required)
else:
    print("you are not eligible")
