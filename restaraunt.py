# Restaraunt
# CS 175-03
# Ez Racancoj

x = 'yes'

while x == 'yes':
        
    vegetarian = False
    vegan = False
    gluten_free = False

    # User input
    response = input('Is anyone in your party a vegetarian ')

    if response == 'yes':
        vegetarian = True
             
    response = input('Is anyone in your party vegan ')

    if response == 'yes':
        vegan = True
            
    response = input('Is anyone in you party gluten-free ')

    if response == 'yes':
        gluten_free = True

    print(
        )



    # Which restaurants can your party go to

    choices = 'Corner Café, ' + 'The Chef’s Kitchen, '
        
    if gluten_free == False and vegan == False and vegetarian == False:
        choices += 'Joe’s Gourmet Burgers, '
        
    if vegan == False and gluten_free == False:
        choices += 'Mama’s Fine Italian, ' + 'Main Street Pizza Company, '
            


    print(f"Here are your restaurant choices: {choices}")


    print(
        )


    v = input('If you want to do another search Enter (yes) if not Enter (no): ')

    if v == 'no':
        x = 'no'


       

