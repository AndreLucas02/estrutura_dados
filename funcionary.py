"""
Crie uma classe chamada Funcionario e outra chamada Departamento.
Na classe Funcionario, inclua os atributos nome, cargo, salario, idade, e data_admissao.
Na classe Departamento, crie uma lista para armazenar os funcionários e implemente os sesguintes métodos
adicionar_funcionario, remover_funcionario, listar_funcionarios, buscar_funcionario, e contar_funcionarios.

"""

class Employee:
    def __init__(self, name, role, salary, age, admission_date):
        self.name = name
        self.role = role
        self.salary = salary
        self.age = age
        self.admission_date =admission_date
        
    def __str__(self) -> str:
        return f' Nome: {self.name}\n Cargo: {self.role}\n Salário: {self.salary}\n Idade: {self.age}\n Data-de-admissão: {self.admission_date}'
    
class Department:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.employees = []
        
    def __str__(self) -> str:
        return f'Departamento {self.name} {self.address}'
    
    def add_employee(self, employee):
        self.employees.append(employee)  
        
    def list_employee(self):
        for employee in self.employees:
            print(f' Nome: {employee.name}, Cargo: {employee.role}, Salário: {employee.salary}, Idade: {employee.age}, Data-de-admissão: {employee.admission_date}')
            
    def search_patient(self, name):
        for employee in self.employees:
            if employee.name == name:
                print('Funcionário encontrado')
                return employee
        return f"Funcionário '{name}' não encontrado na pesquisa"
    
    def remove_patient(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                return f"Funcionario '{name}' removido da lista"
        return f"Funcionário '{name}' não encontrado"
    
    def count_employee(self):
        return len(self.employees)
    
employee01 = Employee('andre', 'programador', 5.000, 27, '20-10-2024')
employee02 = Employee('Joao', 'Técnico em Informática', 3.000, 23, '21-02-2026')

department = Department('Hackers', 'av.Linux, 5566')
print(department)

department.add_employee(employee01)
department.add_employee(employee02)
department.list_employee(),

print(department.search_patient('ze'))
print(department.remove_patient('batista'))

print(department.count_employee())