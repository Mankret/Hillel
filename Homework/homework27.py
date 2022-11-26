# Создать генератор геометрической прогрессии

def new_generator(number_of_elem, first_elem, denominator):
    elem = first_elem
    print(elem)
    for i in range(1, number_of_elem):
        geoprg = elem * denominator
        elem = geoprg
        yield elem


valur = new_generator(5, 1, 7)
for item in valur:
    print(item)