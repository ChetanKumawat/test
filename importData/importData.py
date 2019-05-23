import csv
import MySQLdb


mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='Admin@123',
    db='mydb')
cursor = mydb.cursor()

csv_data = csv.reader(file('/home/bizviz/Downloads/online_univ_learning_data/courses.csv'))
next(csv_data)
for row in csv_data:
    cursor.execute('INSERT INTO courses(course_code,batch_code, length )' 'VALUES("%s", "%s", "%s")', row)
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"
