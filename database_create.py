import pymysql
import logging
import datetime
import os

""" Creating required filename """
filename = os.path.abspath(__file__).split("/")[-1].split(".py")[0] + "_" \
           + datetime.datetime.now().strftime('%m%d%y_%H%M%S')
execution_log =  filename + ".log"


""" Setup logging attributes  """
logging.basicConfig(filename=S, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s: %(message)s', datefmt='%m%d%y %H:%M:%S')

''' Setup logging over console '''
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
def create_connection():
	try:
		mydb = pymysql.connect(host="localhost",user="root",passwd="root123",database="pavan")
		mycursor = mydb.cursor()
		logging.info("created create_connection susfuuly")
		
	except Exception as e:
		logging.error("failed to create new database dute to following error")
		logging.error(str(e))
		return False,False
	return mycursor,mydb


def table_creation(mycursor):
	try:
		mycursor.execute("CREATE TABLE customers7 (name VARCHAR(255), address VARCHAR(255))")
		logging.info("sucessfully created table")
	except Exception as e:
		logging.error(e)
		return False
	return True
	
def insert_data(mycursor,mydb):
	try:
		sql = "INSERT INTO customers7 (name, address) VALUES (%s, %s)"
		val = ("John", "Highway 21")
		mycursor.execute(sql, val)
		mydb.commit()
		logging.info("sucessfully insert data in to table ")
	except Exception as e:
		logging.error(e)
	
if __name__ == '__main__':
	mycursor,mydb=create_connection()
	if mycursor:
		logging.info("statrt table creation")
		table_status=table_creation(mycursor)
		if table_status:
			logging.info("start table insert_data")
			insert_data(mycursor,mydb)
    
