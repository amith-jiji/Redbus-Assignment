from cassandra.cluster import Cluster

clust = Cluster()
session = clust.connect('study_space')

rows = session.execute("SELECT * FROM employee_by_id;")
for row in rows:
    print(str(row.id)+"\t"+row.city+"\t"+row.name+"\t"+str(row.phone)+"\t"+row.position+"\t"+str(row.salary))
print()

session.execute("INSERT INTO employee_by_id(id,city,name,phone,position,salary) VALUES(5,'Kochi','Ajith',8998899811,'Engineering',5000);");
rows = session.execute("SELECT * FROM employee_by_id WHERE id=5;")
for row in rows:
    print(str(row.id)+"\t"+row.city+"\t"+row.name+"\t"+str(row.phone)+"\t"+row.position+"\t"+str(row.salary))
print()

session.execute("UPDATE employee_by_id SET salary = 8000 WHERE id=5;")
rows = session.execute("SELECT * FROM employee_by_id WHERE id=5;")
for row in rows:
    print(str(row.id)+"\t"+row.city+"\t"+row.name+"\t"+str(row.phone)+"\t"+row.position+"\t"+str(row.salary))
print()

rows = session.execute("SELECT * FROM employee_by_id WHERE salary>5000 ALLOW FILTERING;")
for row in rows:
    print(str(row.id)+"\t"+row.city+"\t"+row.name+"\t"+str(row.phone)+"\t"+row.position+"\t"+str(row.salary))
print()


session.execute("DELETE FROM employee_by_id WHERE id=5;")
rows = session.execute("SELECT * FROM employee_by_id;")
for row in rows:
    print(str(row.id)+"\t"+row.city+"\t"+row.name+"\t"+str(row.phone)+"\t"+row.position+"\t"+str(row.salary))
