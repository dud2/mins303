import sqlite3

conn = sqlite3.connect('db.sqlite3')
print ("Opened database successfully")
f = open('vitraj/txt/Imgminer.txt')
for line in f:
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


            
        
