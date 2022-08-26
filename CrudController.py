import CrudView
from Models import Neo4jModel, FileModel


def main():
	while True:
		CrudView.showMenu()
		option = CrudView.getInputAsInt("> ")
		if option == 1:
			# Create an employee record
			CrudView.show(Neo4jModel.create(CrudView.getAllEmployeeValues()))
		elif option == 2:
			# Import records from a file
			for employee in FileModel.importEmployees(CrudView.getInput("Enter path to file or folder: ")):
				CrudView.show(Neo4jModel.create(employee))
		elif option == 3:
			# Retrieve employee records with exact match
			for employee in Neo4jModel.find(CrudView.getExactEmployeeValues(False)):
				CrudView.show(employee)
		elif option == 4:
			# Retrieve employee records with partial match
			for employee in Neo4jModel.find(CrudView.getPartialEmployeeValues()):
				CrudView.show(employee)
		elif option == 5:
			# Retrieve records that contain a field
			for employee in Neo4jModel.findField(CrudView.getInput("What field would you like to search for? "), True):
				CrudView.show(employee)
		elif option == 6:
			# Retrieve records that don't contain a field
			for employee in Neo4jModel.findField(CrudView.getInput("What field would you like to omit? "), False):
				CrudView.show(employee)
		elif option == 7:
			# Count documents that have a given value for a field
			CrudView.show(Neo4jModel.countDocumentsWithValue([CrudView.getInput(
				"What field would you like to search in? "), CrudView.getInput(
				"What value would you like to search for? ")]))
		elif option == 8:
			# View employees hired each year
			for year in Neo4jModel.getEmployeesHiredYear():
				CrudView.show(year)
		elif option == 9:
			# Update the values of an employee record
			CrudView.show(Neo4jModel.update(CrudView.getExactEmployeeValues(True)))
		elif option == 10:
			# Delete an employee record
			Neo4jModel.delete(CrudView.getEmployeeId())
		elif option == 11:
			# Close the application
			break
		else:
			CrudView.showMenu()


main()
