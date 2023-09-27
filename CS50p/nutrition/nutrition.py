#nutrition dictionary lab


fruit_dict = {
    'Apple': '130',
    'Avocado': '50',
    'Banana' : '110',
    'Cantaloupe' : '50',
    'Grapefruit' : '60',
    'Grapes': '90',
    'Honeydew Melon': '50',
    'Kiwifruit': '90',
    'Lemon': '15',
    'Lime' : '20',
    'Nectarine' : '60',
    'Orange' : '80',
    'Peach' : '60',
    'Pear' : '100',
    'Pineapple' : '50',
    'Plums' : '70',
    'Strawberries' : '50',
    'Sweet Cherries' : '100',
    'Tangerine' : '50',
    'Watermelon' : '80',
}



def main():
    i = input("Item: ").title().strip()
    if i in fruit_dict:
        print('Calories:',fruit_dict.get(i))


main()

##below rest my 1 hour.
# fruits_list = [
#     {'fruit': 'Apple', 'calories': '130'},
#     {'fruit': 'Avocado', 'calories': '50'},
#     {'fruit': 'Banana', 'calories': '110'},
#     {'fruit': 'Cantaloupe', 'calories': '50'},
#     {'fruit': 'Grapefruit', 'calories': '60'},
#     {'fruit': 'Grapes', 'calories': '90'},
#     {'fruit': 'Honeydew Melon', 'calories': '50'},
#     {'fruit': 'Kiwifruit', 'calories': '90'},
#     {'fruit': 'Lemon', 'calories': '15'},
#     {'fruit': 'Lime', 'calories': '20'},
#     {'fruit': 'Nectarine', 'calories': '60'},
#     {'fruit': 'Orange', 'calories': '80'},
#     {'fruit': 'Peach', 'calories': '60'},
#     {'fruit': 'Pear', 'calories': '100'},
#     {'fruit': 'Pineapple', 'calories': '50'},
#     {'fruit': 'Plums', 'calories': '70'},
#     {'fruit': 'Strawberries', 'calories': '50'},
#     {'fruit': 'Sweet Cheeries', 'calories': '100'},
#     {'fruit': 'Tangerine', 'calories': '50'},
#     {'fruit': 'Watermelon', 'calories': '80'},
# ]

# for fp in fruits_list:
#     print (fp["fruit"], fp["calories"], 'calories')
