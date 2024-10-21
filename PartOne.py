camel_case_input = input("Enter a variable name in camel case: ")

snake_case = ""

for c in camel_case_input:
    if c.isupper():
        snake_case += "_" + c.lower()
    else:
        snake_case += c

print("The variable name in snake case is:", snake_case)

