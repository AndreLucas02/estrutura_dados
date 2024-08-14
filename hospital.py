"""
Crie uma classe chamada Paciente e outra chamada Hospital.
Na classe Paciente, inclua os atributos nome, idade, e diagnostico.
Na classe Hospital, crie uma lista para armazenar os pacientes e implemente os seguintes métodos
adicionar_paciente, remover_paciente, listar_pacientes, buscar_paciente, e contar_pacientes.

"""


class Patient:
    def __init__(self, name, age, diagnostic):
        self.name = name
        self.age = age
        self.diagnostic = diagnostic
        
    def __str__(self) -> str:
        return f' Nome do Paciente: {self.name}\n Idade: {self.age}\n Diagnóstico: {self.diagnostic}'

class Hospital:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.patients = []
        
    def __str__(self) -> str:
        return f' Hospital {self.name} {self.address}'

    def add_patient(self, patient):
        self.patients.append(patient)

    def remove_patient(self, name):
        for patient in self.patients:
            if patient.name == name:
                self.patients.remove(patient)
                return f'Paciente {name} removido da lista'
        return f'Paciente {name} não foi encontrado'

    def list_patients(self):
        for patient in self.patients:
            print(f"Nome: {patient.name}, Raça: {patient.age}, Idade: {patient.diagnostic}")

    def search_patient(self, name):
        for patient in self.patients:
            if patient.name == name:
                print('Paciente encontrado')
                return patient
        return f" O paciente '{name}' não existe nessa lista"

    def count_patient(self):
        return len(self.patients)

id_01 = Patient('Jose da Mandioca', 65, 'Labiritinte')
id_02 = Patient('Maria das Dores', 56, 'hipertensa')
id_03 = Patient('Camila Barros', 25, 'Amor demais')

hostipal = Hospital('João Paulo II', 'Av. campo sales - 2258 porto velho - RO')
print(hostipal)

hostipal.add_patient(id_01)
hostipal.add_patient(id_02)
hostipal.add_patient(id_03)
hostipal.list_patients()

print('-' * 50)
print(hostipal.search_patient('Jose da Mandioca'))

print(hostipal.remove_patient('rato'))

print(hostipal.count_patient())
