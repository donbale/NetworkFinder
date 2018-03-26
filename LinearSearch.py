def linearSearch(item, my_list):
    position = 0
    while position < len(my_list):
        if my_list[position] == item:
            return True
        position = position + 1
    return False

def main():
    bag = ['book', 'pencil', 'pen', 'note book', 'sharpener', 'rubber']
    item = input('What item do you want to check for in the bag? ')
    itemFound = linearSearch(item, bag)

    if itemFound:
        print('Yes, the item is in the bag')
    else:
        print('Oops, your item seems not to be in the bag')

if __name__ == '__main__':
    main()

