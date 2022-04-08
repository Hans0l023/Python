items = []
item = None
total_cost = []
cost = 0
action = False

while action != True:
    print('Please select one of the following: ')
    print('1. Add Item')
    print('2. View Cart')
    print('3. Remove Item')
    print('4. Compute total')
    print('5. Quit')
    action = input('PLease enter an action: ')

    if action == '1':
        print('What is in the cart? Type done when finished')

        item = input('What will you add to the cart? ').title()
        if item != 'Done':
            cost = float(input(f'What is the cost of {item}? '))
            print(f'{item} has been added to the cart.')
            items.append(item)   
            total_cost.append(cost)
            print()
    
    elif action == '2':
        print()
        print('The Items in the cart are:')


        for i in range(len(items)):
            item = items[i]
            cost = total_cost[i]
            print(f'{i + 1}: {item:20}: {cost}')

    elif action == '3':
        removed = int(input(f'From 1 - {len(items)} wich will you remove? '))
        items.pop(removed - 1)
        total_cost.pop(removed - 1)
        print('Your new list is')
        for i in range (len(items)):
            item = items[i]
            cost = total_cost[i]
            print(f'{i + 1}: {item:20}: {cost}')
                
    elif action == '4':
        amount = sum(total_cost)
        print(f'Your total is {amount:.2f}')

    else:
        action = True 
        print('Thank you goodbye.')



