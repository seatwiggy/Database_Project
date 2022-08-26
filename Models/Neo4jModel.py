from neo4j import GraphDatabase

graph = GraphDatabase.driver('bolt:localhost:7687/people', auth=('neo4j', 'password'))


def create(employee):
    with graph.session() as session:
        return session.run("CREATE (a:Employee {" +
                           "firstName: '" + employee["firstName"] +
                           "', lastName: '" + employee["lastName"] +
                           "', hireYear: '" + employee["hireYear"] +
                           "', id_: '" + employee["_id"] + "'}) RETURN a").single()[0]


def delete(employeeId):
    with graph.session() as session:
        session.run("MATCH (a:Employee) WHERE a.id_ = '" + employeeId + "' DELETE a")


def update(employee):
    with graph.session() as session:
        return session.run("MATCH (a:Employee) WHERE a.id = '" + employee["id_"] + "' SET a = {" +
                           "firstName: '" + employee["firstName"] +
                           "', lastName: '" + employee["lastName"] +
                           "', hireYear: '" + employee["hireYear"] +
                           "', id_: '" + employee["_id"] + "'} RETURN a").single()[0]


def find(employee):
    firstName = "a.firstName = '" + employee["firstName"] + "'" if "firstName" in employee else ""
    lastName = "a.lastName = '" + employee["lastName"] + "'" if "lastName" in employee else ""
    hireYear = "a.hireYear = '" + employee["hireYear"] + "'" if "hireYear" in employee else ""
    id_ = "a.id_ = '" + employee["_id"] + "'" if "_id" in employee else ""
    with graph.session() as session:
        return session.run("MATCH (a:Employee) WHERE " + firstName + " AND " if firstName else "" + lastName + " AND " if lastName else "" + hireYear + " AND " if hireYear else "" + id_ + " RETURN a").single()[0]


def findField(field, exists):
    finding = "NOT" if exists else ""
    with graph.session() as session:
        return session.run(f"match (a:Employee) where (a.{field}) is {finding} null return a").single()


def countDocumentsWithValue(employee):
    with graph.session() as session:
        return session.run("MATCH (a:Employee) WHERE a." + employee[0] + " = '" + employee[1] + "' RETURN a").single()[
            0]


def getEmployeesHiredYear():
    with graph.session() as session:
        return session.run("MATCH (a:Employee) RETURN a.hireYear AS hireYear, count(a) AS count").single()[0]
