def notebooks(weight_pulp):
    num_of_notebooks = 10 * weight_pulp
    return num_of_notebooks
weight_pulp = float(input("Enter the weight of pulp in kilograms: "))
result=notebooks(weight_pulp)
print("The number of notebooks:", result)
