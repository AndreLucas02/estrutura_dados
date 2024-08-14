class Pilha:
  def __init__(self):
     self.itens = []
  
  def push(self, item):
     self.itens.append(item)
  
  def pop(self):
     self.itens.pop()

  def exibir_pilha(self):
     for item in self.itens[::-1]:
         print(item)
  def size(self):
     print(len(self.itens)) 
  def peek(self):
     print(self.itens[-1])
  def is_empty(self):
        if len(self.itens) == 0:
           print('lista vazia')
        else:
           print('lista não está vazia')

pilha = Pilha()

pilha.push('primeiro')
pilha.push('segundo')
pilha.push('terceiro')
pilha.exibir_pilha()


pilha.pop()
print('------------------')
pilha.exibir_pilha()
pilha.pop()
print('-------------------')
pilha.exibir_pilha()
pilha.size()
pilha.peek()
pilha.is_empty()