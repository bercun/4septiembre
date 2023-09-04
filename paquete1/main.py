import  users.modulo_cliente 
from users.gustmusic import *

clien1 = users.modulo_cliente.Cliente("Walter", "Bercunchelli", "0992525", "wal@gmail.com", "credit card", ["metal", "rock", "tecno", "hevy metal"])
clien2 = Cliente("Patricia", "Pata", "0992526", "Pata@gmail.com", "devito bancario", ["rock","lentas", "regueton," "plena"])
clien3 = Cliente("Diego", "Bercunchelli", "0992527", "diego@gmail.com", "efectivo", ["rock", "reggae","hevy metal", "country"])
clien4 = Cliente("Hueso", "Galan", "0992528", "hueso@gmail.com", "transferencia bancaria ", ["canto popular", "candombe", "rock","plena"])
clien5 = Cliente("Nahuel", "Pouso", "0992529", "Nahuel.Pouso@gmail.com", "Transferencia Bancaria", ["rock", "tecno","hevy metal", "country"] )


print(f"Lista de clientes \n{clien1.nombre} \n{clien2.nombre} \n{clien3.nombre} \n{clien4.nombre} \n{clien5.nombre} ") 


#Walter=clien1
#Patricia=clien2
#Diego=clien3
#Hueso=clien4

var_cli=input("Ingresa el nombre de cliente:")
var_genero=input("ingresar genero de musica :")

#var_cli.gusmus(var_genero)


#print (f"el nuevo cliente es: \n{clien5.nombre}")

