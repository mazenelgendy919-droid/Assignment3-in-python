students = [{ "name" : "mazen" , "grades" : [80 , 90 , 100]},
{ "name" : "ahmed" , "grades" : [70 , 65 , 80]},
{ "name" : "said" , "grades" : [60 , 75 , 85]}]
for student in students:
    avg_grade = sum(student["grades"]) / len(student["grades"])
    print(f"The average grade of {student['name']} is {avg_grade}")