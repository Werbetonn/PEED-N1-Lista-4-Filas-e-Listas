class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]


fila = Queue()

print("Digite uma sequência de números inteiros e finalize com um número negativo):")

while True:
    numero = int(input())
    if numero < 0:
        break
    fila.enqueue(numero)

print("\nOS elementos da fila são:")

while not fila.is_empty():
    elemento = fila.dequeue()
    print(elemento)