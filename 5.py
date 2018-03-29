/*Proszę zaimplementować funkcję przyjmującą jako argument listę liczb całkowitych. Funkcja powinna zwracać znormalizowaną listę, utworzoną w taki sposób, aby największy co do wartości element miał wartość równą (co do wartości bezwzględnej)*/

def five(*list):
newList = []
max = max(list)
min = min(list)
dzielnik = max(abs(max),abs(min))

for i in range(0,len(list)):
    newList.append(list[i]/dzielnik)

print newList
