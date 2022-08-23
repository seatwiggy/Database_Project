from pymongo import MongoClient

client = MongoClient("mongodb://localhost:2717/")
database = client["CrudBusiness"]
collection = database["employees"]


def create(employee):
	return f'Created employee with id {collection.insert_one(employee).inserted_id}'


def delete(employeeId):
	collection.delete_one({"_id": employeeId})


def update(employee):
	employeeId = employee.pop("_id")
	collection.update_one({"_id": employeeId}, {"$set": employee})
	return f"Updated employee {employeeId} with values {employee}"


def find(employee):
	return collection.find(employee)


def findField(field, exists):
	return collection.find({field: {"$exists": exists}})


def countDocumentsWithValue(employee):
	return f"{collection.count_documents(employee)} documents found"


def getEmployeesHiredYear():
	return collection.aggregate([{"$group": {"_id": "$hireYear", "count": {"$sum": 1}}}])
