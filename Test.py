import mysql.connector

mydb = mysql.connector.connect(  ## Creación de la conexión con la base de datos
    host = "localhost",
    user = "root",
    passwd = "07081998",
    database = "python_db"
)

micursor = mydb.cursor() ## Se crea un cursor

micursor.execute("SELECT * FROM hospital;")  ##Mediante el cursor le pasamos el select que queremos que se ejecute en la base de datos

resultados = micursor.fetchall() ## Asignamos a la variable resultados lo que obtenemos de la base de datos mediane el metodo fetchall() en el cursor que hemos creado

for resultado in resultados:  ##Printeamos los resultados de la consulta
    print(resultado)

consultaSql = "INSERT INTO hospital (Hospital_Id, Hospital_Name, Bed_Count) VALUES ('5', 'Damo Clinic', '2000');"  ## Metemos el insert en un String

micursor.execute(consultaSql) ## Pasamos el String al metodo execute del cursor

mydb.commit() ## Mediante el commit "actualizamos" la info en la BBDD y el insert surte efecto

consultaVariables = "INSERT INTO hospital (Hospital_Id, Hospital_Name, Bed_Count) VALUES (%s, %s, %s);", (id,nombre,camas) ## Valores mediante variables que se difiniran más adelante

valores = (id,nombre,camas)

micursor.execute(consultaVariables, valores)

mydb.commit

text = input("Dame texto ")

if("esto" in text):
    print("Estoy dentro del if")