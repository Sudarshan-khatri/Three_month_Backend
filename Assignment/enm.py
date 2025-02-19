list1=[1,3,5,7,9,"sudarshan","khatri"]
print(list(enumerate(list1,start=100)))



list2=[1,3,4,'hi',"hello"]
for student_id ,name in enumerate(list2,start=100):
    print("Student_id:{} \t  Name:{}".format(student_id,name))
