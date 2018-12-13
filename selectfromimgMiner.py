import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
print ("Opened database successfully")
sql = "Select * From Vitraj_Imgminer"
for row in cursor.execute(sql):
    print(row)

            
        
