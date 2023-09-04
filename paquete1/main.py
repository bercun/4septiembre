import  users.modulo_cliente 

clien1 = users.modulo_cliente.Cliente("Walter", "Bercunchelli", "0992525", "wal@gmail.com", "credit card", ["metal", "rock", "tecno", "hevy metal"])
clien2 = users.modulo_cliente.Cliente("Patricia", "Pata", "0992526", "Pata@gmail.com", "devito bancario", ["rock","lentas", "regueton," "plena"])
clien3 = users.modulo_cliente.Cliente("Diego", "Bercunchelli", "0992527", "diego@gmail.com", "efectivo", ["rock", "reggae","hevy metal", "country"])
clien4 = users.modulo_cliente.Cliente("Hueso", "Galan", "0992528", "hueso@gmail.com", "transferencia bancaria ", ["canto popular", "candombe", "rock","plena"])
clien5 = users.modulo_cliente.Cliente("Nahuel", "Pouso", "0992529", "Nahuel.Pouso@gmail.com", "Transferencia Bancaria", ["rock", "tecno","hevy metal", "country"] )


print(f"Lista de clientes \n{clien1.nombre} \n{clien2.nombre} \n{clien3.nombre} \n{clien4.nombre}") 



#print (f"el nuevo cliente es: \n{clien5.nombre}")

