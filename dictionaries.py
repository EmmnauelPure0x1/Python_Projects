# What is a Dictionary ?

# Dictionary is a set of data which operate as a Key Value Pair
# Dictionaries (arrays) is another way of managing data but more dynamically.

# Syntax: {"key":"value", key:"value"}
# What type of data can we store/manage


# Dictionary #1
devops_student_data = {
    "name": "Emmanuel",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_name": ["operators", "data_types", "variables"]
}

print(type(devops_student_data))
print(devops_student_data)

# Name
print(devops_student_data["name"])

# changing name value
devops_student_data["name"] = "BabaJide"
print(devops_student_data["name"])
print("\n")

# print keys or values from dict
print(devops_student_data.keys())
print(devops_student_data.values())

# How can we fetch the value called data types
print(devops_student_data["completed_lesson_name"][2])
print(devops_student_data["completed_lesson_name"][:1])
print(devops_student_data["completed_lesson_name"][:])