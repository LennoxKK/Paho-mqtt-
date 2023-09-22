
import time
import os
querry = f"select * from pub_sub_msg"


from mysql_connector import cursor,db
cursor.execute("select * from pub_sub_msg")
#cursor.execute("refresh table pub_sub_msg")
data = cursor.fetchall()
os.system('clear')
for i in data:
    print(i[0])
print("\n{} topics now!".format(len(data)))
time.sleep(3)
os.system('clear')
print("loading..")
time.sleep(3)
os.system('python livestream.py')