#defino una funcion para pedir y guardad nombre de usuario y contraseña

def  registro(n):

  usr_data = {}
  while n>0:
    user = input("Ingresar nombre de usuario : ")
    passw = input("ingresar password : ")
    usr_data[user] = passw
    n -=1
  return usr_data
#creo un diccionario para usarla como base de datos
db_usr_data = (registro (2))
db_usr_data_str = db_usr_data.co
db_usr_data_str = str(db_usr_data_str)


miArchivo = open("./usuar_pass.txt" , "a") #creo un archivo en modo "a" para poder ir guardando mis usr, passw, actualizandose cada vez que ingreso datos nuevos, sin que se sobre escriban
miArchivo.write(db_usr_data_str)
miArchivo.close()
