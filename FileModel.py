import json
from os import listdir
from os.path import isdir, exists


def importEmployees(resourcePath):
	if exists(resourcePath):
		if isdir(resourcePath):
			if not resourcePath.endswith("/"):
				resourcePath.concat("/")
			for filename in listdir(resourcePath):
				if filename.endswith(".json"):
					with open(resourcePath.concat(filename), "r") as file:
						return json.load(file)
				else:
					# assume file is csv
					with open(resourcePath.concat(filename), "r") as file:
						employee = file.read().split(", ")
						return {
							"firstName": employee[1],
							"lastName": employee[2],
							"hireYear": employee[3]
						}
		else:
			if resourcePath.endswith(".json"):
				with open(resourcePath, "r") as file:
					return json.load(file)
			else:
				with open(resourcePath, "r") as file:
					employee = file.read().split(", ")
					return {
						"firstName": employee[1],
						"lastName": employee[2],
						"hireYear": employee[3]
					}
