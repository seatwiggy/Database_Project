import CrudView
import FileModel
import MongoModel


def main():
	while True:
		CrudView.showMenu()
		option = CrudView.getInputAsInt("> ")
		match option:
			case 1:
				# Create an employee record
				CrudView.show(MongoModel.create(CrudView.getAllEmployeeValues()))
			case 2:
				# Import records from a file
				for employee in FileModel.importEmployees(CrudView.getInput("Enter path to file or folder: ")):
					CrudView.show(MongoModel.create(employee))
			case 3:
				# Retrieve employee records with exact match
				for employee in MongoModel.find(CrudView.getExactEmployeeValues(False)):
					CrudView.show(employee)
			case 4:
				# Retrieve employee records with partial match
				for employee in MongoModel.find(CrudView.getPartialEmployeeValues()):
					CrudView.show(employee)
			case 5:
				# Retrieve records that contain a field
				for employee in MongoModel.findField(CrudView.getInput("What field would you like to search for? "), True):
					CrudView.show(employee)
			case 6:
				# Retrieve records that don't contain a field
				for employee in MongoModel.findField(CrudView.getInput("What field would you like to omit? "), False):
					CrudView.show(employee)
			case 7:
				# Count documents that have a given value for a field
				CrudView.show(MongoModel.countDocumentsWithValue({CrudView.getInput(
					"What field would you like to search in? "): CrudView.getInput(
					"What value would you like to search for? ")}))
			case 8:
				# View employees hired each year
				for year in MongoModel.getEmployeesHiredYear():
					CrudView.show(year)
			case 9:
				# Update the values of an employee record
				CrudView.show(MongoModel.update(CrudView.getExactEmployeeValues(True)))
			case 10:
				# Delete an employee record
				MongoModel.delete(CrudView.getEmployeeId())
			case 11:
				# Close the application
				break
			case _:
				CrudView.showMenu()


main()
