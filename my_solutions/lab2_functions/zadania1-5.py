def test(fun, *args):
    print "".join(['-' for i in range(40)])
    print fun.__name__[:-1].upper()+" "+fun.__name__[-1]
    res = fun(*args[:-1])
    if isinstance(args[0], str):
        decoded = "".join([chr(i) for i in args[-1]])
        if res == decoded:
            print "Yes, "+decoded.replace("my","your")
        else:
            print "No, "+decoded.replace("my","your").replace("has","has not")+" yet"
    else:
        print "Is correct? "+ str(res == args[-1])
    print "".join(['-' for i in range(40)])

def zadanie1(listObject):
    a = []
    a.append(listObject[0])
    c = listObject[0]
    for element in listObject:
        if element != c:
            a.append(element)
            c = element
    return a

test(zadanie1, [1, 1, 1, 1, 1, 1, 1, 1], [1])

def zadanie2(list1, list2):
    new = []
    min_length = min(len(list1), len(list2))

    for i in range(min_length):
        new.append(list1[i])
        new.append(list2[i])

    new.extend(list1[min_length:])
    new.extend(list2[min_length:])

    return new

test(zadanie2, [1, 2, 19, 'dd', ':P', ":("], [12,'c','5'], [1, 12, 2, 'c', 19, '5', 'dd', ':P', ':('])

def zadanie3(listTuples):
    sorted_list = sorted(listTuples, key=lambda x: x[-1])
    return sorted_list

test(zadanie3, [(1, 3), (3, 3, 2), (2, 1)], [(2, 1), (3, 3, 2), (1, 3)])

# zadanie 4 zrobione lopatologicznie
# def zadanie4(text):
#     result = str()
#     for i in range(len(text)):
#         if text[i] == "o" and text[i+1] == "k":
#             count = i + 2
#             while text[count] != "$":
#                 result += text[count]
#                 count += 1
#             result += " "
#     return result

def zadanie4(text):
    text = text.replace("ok", " ")
    lista = text.split("$")
    lista = [s for s in lista if s.startswith(" ")]
    return ("".join(lista)).strip()

test(zadanie4, "okmy$aiaetiaigaafbaf??a$okwatch$oafbusd$okhas$asbrsi31480$okended$aq340af", [109, 121, 32, 119, 97, 116, 99, 104, 32, 104, 97, 115, 32, 101, 110, 100, 101, 100])

# zadanie 5
from random import randint

drawn = randint(1, 9)
user_type = input("Podaj liczbe z zakresu od 1 do 9:\n")
# print "Podales " + str(a)

while user_type < 1 or user_type > 9:
    user_type = input("Podaj liczbe z wlasciwego zakresu:\n")

while not user_type == drawn:
    if user_type > drawn:
        print "Troche za duzo"
    else:
        print "Troche za malo"

    user_type = input("Probuj dalej:\n")

print "Swietnie, udalo Ci sie zgadnac.\n", "Szukana liczba to: " + str(drawn)