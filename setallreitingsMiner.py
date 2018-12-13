import sqlite3

conn = sqlite3.connect('db.sqlite3')
print ("Opened database successfully")
cursor = conn.cursor()
cursor1 = conn.cursor()
sumrei = 0.0
for row in cursor.execute("Select * From Vitraj_Imgminer"):
        n = row[2]
        pr = row[5]
        if pr==3:
                pr=4
        rei = 0         
        rei += 0.2/pr
#        print(rei)
        sql = "Select * From Vitraj_Chemform Where Name=?"
        for row1 in cursor1.execute(sql, [(n)]):
                fo = row1[3]
                if(len(fo)!=0):
                        rei+=0.2/pr
#        print(rei)
        sql = "Select * From Vitraj_Interface Where Name=?"
        for row1 in cursor1.execute(sql, [(n)]):
                nam = row1[2]
#                print(nam)
                if(len(nam)!=0):
                        rei+=0.1/pr
#        print(rei)
        sql = "Select * From Vitraj_Physic Where Name=?"
        for row1 in cursor1.execute(sql, [(n)]):
                nam = row1[2]
#                print(nam)
                if(len(nam)!=0):
                        rei+=0.01/pr
#        print(rei)
        sql = "Select * From Vitraj_Chemical Where Name=?"
        for row1 in cursor1.execute(sql, [(n)]):
                nam = row1[2]
#                print(nam)
                if(len(nam)!=0):
                        rei+=0.01/pr
#        print(rei)
        
        sql = "UPDATE Vitraj_Imgminer SET Reiting =? WHERE Name =?"
        params = (rei,n) 
        cursor1.execute (sql, params)
        sumrei +=rei

        """
    print(line)
    p = line.split(';')
    t = p[0]
    n = p[1]
    e = p[2]
    i = p[3]
    pr = p[4]
    r = p[5]
    sql = "insert into Vitraj_Imgminer (MId, Name, Enname, Ischange, Prior, Reiting) values (?, ?, ?, ?, ?, ?)"
    params = (t, n, e, i, pr, r)  
    conn.execute(sql, params)
    conn.commit()
f.close()
"""
conn.commit()
print("Суммарный рейтинг = ", sumrei)
print("Cymmaрный рейтинг в процентах = ", sumrei*100/303)


            
        
