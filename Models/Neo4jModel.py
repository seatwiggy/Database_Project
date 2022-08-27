import re

from neo4j import GraphDatabase

graph = GraphDatabase.driver('bolt:localhost:7687/people', auth=('neo4j', 'password'))


def create(employee):
    with graph.session() as session:
        return session.run("CREATE (a:Person {" +
                           "firstName: '" + employee["firstName"] +
                           "', lastName: '" + employee["lastName"] +
                           "', hireYear: '" + employee["hireYear"] +
                           "', id: '" + employee["_id"] + "'}) RETURN a").single()[0]


def delete(employeeId):
    with graph.session() as session:
        session.run("MATCH (a:Person) WHERE a.id_ = '" + employeeId + "' DELETE a")


def update(employee):
    with graph.session() as session:
        return session.run("MATCH (a:Person) WHERE a.id = '" + employee["id_"] + "' SET a = {" +
                           "firstName: '" + employee["firstName"] +
                           "', lastName: '" + employee["lastName"] +
                           "', hireYear: '" + employee["hireYear"] +
                           "', id: '" + employee["_id"] + "'} RETURN a").single()


def find(employee):
    firstName = "a.firstName = '" + employee["firstName"] + "'" if "firstName" in employee else ""
    lastName = "a.lastName = '" + employee["lastName"] + "'" if "lastName" in employee else ""
    hireYear = "a.hireYear = '" + employee["hireYear"] + "'" if "hireYear" in employee else ""
    id_ = "a.id = '" + employee["_id"] + "'" if "_id" in employee else ""
    query = ("MATCH (a:Person) WHERE " + firstName + (" AND " if firstName != "" else "") + lastName + (" AND " if lastName != "" else "") + hireYear + (" AND " if hireYear != "" else "") + id_ + " RETURN a")
    print(query)
    with graph.session() as session:
        results = session.run(query).single()[0]
        props = re.match(r".*properties=(\{.*}).*", str(results))

        return props.group(1).split(",") if props else []


def findField(field, exists):
    finding = "NOT" if exists else ""
    with graph.session() as session:
        return session.run(f"MATCH (a:Person) WHERE a.{field} IS {finding} NULL RETURN a").single()


def countDocumentsWithValue(employee):
    with graph.session() as session:
        return session.run("MATCH (a:Person) WHERE a." + employee[0] + " = '" + employee[1] + "' RETURN a").single()[0]


def getEmployeesHiredYear():
    with graph.session() as session:
        return session.run("MATCH (a:Person) RETURN a.hireYear AS hireYear, count(a) AS count").single()[0]
