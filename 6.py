/* Proszę zaimplementować funkcję losowanieLotto. Funkcja powinna przyjmować jako argument łańcuch znaków. W przypadku otrzymania wartości ‘Lotto’ funkcja powinna zwracać listę 6-ciu liczb losowych z przedziału <1,49>. W przypadku argumentu o wartości ‘Multi Multi’ funkcja powinna zwracać 20-to elementową listę utworzoną ze zbioru liczb <1,80>. W przypadku podania nieobsługiwanej wartości funkcja powinna zwrócić napis „Nie oferujemy takiej gry. Zapraszamy do gry w ‘Lotto’ lub ‘Multi Multi’” 
       http://www.lotto.pl/multi-multi/jak-grac-w-multi-multi */


import random 

def losowanieLotto(los):
    if los == "Lotto":
        return random.sample(range(1,50), 6)
    elif los == "Multi Multi":
        return sorted(random.sample(range(1,81), 20))
    else:
        return "Nie oferujemy takiej gry. Zapraszamy do gry w \"Lotto\" lub \"Multi Multi\""
