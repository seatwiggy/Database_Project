menu = """
What would you like to do?
1)  Create an employee record
2)  Import records from a file
3)  Retrieve employee records with exact match
4)  Retrieve employee records with partial match
5)  Retrieve records that contain a field
6)  Retrieve records that don't contain a field
7)  Count documents that have a given value for a field
8)  View employees hired each year
9)  Update the values of an employee record
10) Delete an employee record
11) Close the application
"""


def show(item):
	print(item)


def getInput(prompt):
	return input(prompt)


def getInputAsInt(prompt):
	return int(getInput(prompt))


def showMenu():
	print(menu)


def getAllEmployeeValues():
	return {
		"firstName": input("What is the employee's first name? "),
		"lastName": input("What is the employee's last name? "),
		"hireYear": input("What is the employee's hire year? "),
		"_id": input("What is the employee's id? ")
	}


def getExactEmployeeValues(requireId):
	employee = {}

	if requireId:
		employee["_id"] = input("What is the id of this employee? ")
	else:
		employeeId = input("What is the id of this employee? (Press Enter to omit field) ")
		if employeeId.strip() != "":
			employee["_id"] = employeeId

	employeeFirstName = input(
		"What is the first name of this employee? (Press Enter to omit field) ")
	if employeeFirstName.strip() != "":
		employee["firstName"] = employeeFirstName

	employeeLastName = input(
		"What is the last name of this employee? (Press Enter to omit field) ")
	if employeeLastName.strip() != "":
		employee["lastName"] = employeeLastName

	employeeHireYear = input(
		"What is the hire year of this employee? (Press Enter to omit field) ")
	if employeeHireYear.strip() != "":
		employee["hireYear"] = employeeHireYear

	return employee


def getPartialEmployeeValues():
	employee = {}

	employeeId = input("What is the id of the employee you would like to find? (Press Enter to omit field) ")
	if employeeId.strip() != "":
		employee["_id"] = "/" + employeeId + "/"

	employeeFirstName = input(
		"What is the first name of the employee you would like to find? (Press Enter to omit field) ")
	if employeeFirstName.strip() != "":
		employee["firstName"] = "/" + employeeFirstName + "/"

	employeeLastName = input(
		"What is the last name of the employee you would like to find? (Press Enter to omit field) ")
	if employeeLastName.strip() != "":
		employee["lastName"] = "/" + employeeLastName + "/"

	employeeHireYear = input(
		"What is the hire year of the employee you would like to find? (Press Enter to omit field) ")
	if employeeHireYear.strip() != "":
		employee["hireYear"] = "/" + employeeHireYear + "/"

	return employee


def getEmployeeId():
	return input("What is this employee's id? ")
