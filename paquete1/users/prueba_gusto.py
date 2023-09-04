class Cliente:
    def __init__(self, nombre, apellido, telefono, email, forma_de_pago_, tipo_musica=[]):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.email=email
        self.tipo_musica=tipo_musica
        self.forma_de_pago=forma_de_pago_
    
    def __str__ (self):
        return f"apellido del cliente {self.apellido}"

    def gusmus(self, music):
        for genero in self.tipo_musica:
            if music == genero:
              print (f'Al clien1 le gusta el rock')
              break    
        
        
clien1 = Cliente("Walter", "Bercunchelli", "0992525", "wal@gmail.com", "credit card", ["metal", "rock", "tecno", "hevy metal"])
#clien2 = Cliente("Patricia", "Pata", "0992526", "Pata@gmail.com", "devito bancario", ["rock","lentas", "regueton," "plena"])
#clien3 = Cliente("Diego", "Bercunchelli", "0992527", "diego@gmail.com", "efectivo", ["rock", "reggae","hevy metal", "country"])
#clien4 = Cliente("Hueso", "Galan", "0992528", "hueso@gmail.com", "transferencia bancaria ", ["canto popular", "candombe", "rock","plena"])
#clien5 = Cliente("Nahuel", "Pouso", "0992529", "Nahuel.Pouso@gmail.com", "Transferencia Bancaria", ["rock", "tecno","hevy metal", "country"] )

clien1.gusmus("rock")