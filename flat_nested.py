"""
Flat vs nested data (date uniforme vs date imbricate)
Flat data = date uniforme, structuri de date (colectii) care au ca elemente
            date primitive (basic date types) 
Nested date = date imbricate, structuri de date (colectii) care au ca elemente
            alte colectii de date = liste de liste, dictionare in care valorile
            sunt la randul lor dictionare

"""
flat_list = [2, 5, 7, 9]
flat_list2 = ['Paris', 'Roma', 'Berlin']
flat_dict = {
    'name': 'Jhon Doe',
    'age': 20,
    'address_street': 'The Street',
    'address_number': 20,
    'salary': 2500
}
flat_dict2 = {
    'name': 'Jhon Doe',
    'age': 20,
    'address_street': 'The Street',
    'address_number': 20,
    'salary': 2500
}

nested_list = [[4, 5], [9, 20], [3, 10]]
print(f'Elementul cu index 0 din a adoua sublista: {nested_list[1][0]}')
nested_dict = {
    'name': 'Jhon Doe',
    'age': 20,
    'address': {
        'street': 'The Street',
        'number': 20
    },
    'salary': 2500
}
print(f'Valoarea asociata cheii adress este: {nested_dict["address"]}')
print(f'Valoarea asociata cheii adress este:'
      f'{nested_dict["address"]["street"]}')

# conversia unei liste imbricate  / nested la o lista flat / uniforme
flattened_list = []
for sublist in nested_list:
    print(sublist)
    for element in sublist:
        flattened_list.append(element)
print(f'Lista nested: {nested_list}')
print(f'Lista flat: {flattened_list}')

flattened_list2 = [element for sublist in nested_list for element in sublist]
print(f'Lista flat: {flattened_list2}')
