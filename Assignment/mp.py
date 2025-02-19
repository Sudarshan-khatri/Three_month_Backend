def my_map(x):
    if x>22:
        return True
    else:
        return False
    

ages=[2,22,33,44,55,67,78]
my_ages=map(my_map,ages)

for x in my_ages:
    print(list(my_ages))