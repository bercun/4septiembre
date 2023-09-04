#Defino una funcion para la comprobacion de usuario y contraseña

def login(usr_in, passw_in):
  if usr_in in db_usr_data and db_usr_data[usr_in] == passw_in:
    return True

  else:
    return False
# Creo una varialbe n para contar los intentos erroneos
n=3
# Con el while creo un bucle que pide usuario y contraseña para comprobarlo con la funcion login
while n  > 0 :
    usr_in = input("Ingresar usuario : ")
    passw_in = input("Password : ")

    if login(usr_in, passw_in):
      print("Entrando al sitema \nBien venido")

      break

    else:
      n -=1
      print("Inicio erroneo, intentelo de nuevo ")

if n==0:
  print("Sitema bloqueado, por exeso de intentos")


