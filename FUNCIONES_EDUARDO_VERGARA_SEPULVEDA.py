lista_paciente = []
import random
def Registrar_Cobro(lista_paciente):
   Dhospitalado =random.randrange(1,10)

   nompaciente = input("Ingrese el nombre del paciente:")
   apepaciente = input("Ingrese el apellido del paciente:")
   dirpaciente = input("Ingrese la direccion del paciente:")
   costinsumos = int(input("Ingrese los costos de insumo"))
   bene = (Dhospitalado * 90000 + costinsumos) * 0.70 
   tot = (Dhospitalado * 90000 + costinsumos) - bene
   
   paciente = ("Nombre del paciente":nompaciente,"Apellido del paciente":apepaciente,"Direccion del paciente":dirpaciente,"Dias Hospitalados",Dhospitalado,"Costos de Insumos",csotisumos)
   lista_paciente.append(paciente)


