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
        


#print(f"Lista de clientes {clien1.nombre} \n{clien2.nombre} \n{clien3.nombre} \n{clien4.nombre}") 
#print(f"Formas de pago preferidas {clien1.forma_de_pago}\n {clien2.forma_de_pago} \n{clien3.forma_de_pago} \n{clien4.forma_de_pago}")

#print(clien1.nombre)
