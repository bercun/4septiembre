import modulo_cliente

clien1 = modulo_cliente.Cliente("Walter", "Bercunchelli", "0992525", "wal@gmail.com", "credit card", ["metal", "rock", "tecno", "hevy metal"])
clien2 = modulo_cliente.Cliente("Patricia", "Pata", "0992526", "Pata@gmail.com", "devito bancario", ["rock","lentas", "regueton," "plena"])
clien3 = modulo_cliente.Cliente("Diego", "Bercunchelli", "0992527", "diego@gmail.com", "efectivo", ["rock", "reggae","hevy metal", "country"])
clien4 = modulo_cliente.Cliente("Hueso", "Galan", "0992528", "hueso@gmail.com", "transferencia bancaria ", ["canto popular", "candombe", "rock","plena"])
clien5 = modulo_cliente.Cliente("Nahuel", "Pouso", "0992529", "Nahuel.Pouso@gmail.com", "Transferencia Bancaria", ["rock", "tecno","hevy metal", "country"] )

print (f'este es el cliente {clien1.tipo_musica}')
