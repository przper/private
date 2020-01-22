def DisplayOptions(options):
    for i in range(len(options)):
        print("{} - {}".format(i+1, options[i]))
    choice = input('Select options above or press enter to exit: ')
    return choice

options = ['load data', 'export data', 'analyze & predict']
choice = 'x'

while choice:
    choice = DisplayOptions(options)
    #executed only if something was entered
    if choice:
        try:
            choice_num=int(choice)-1
            if choice_num>=0 and choice_num<len(options):
                print("you have selected {} - {}".format(choice_num+1,options[choice_num]))
            else:
                print("choose a value from a list or press enter")
        except:
            print("you need to enter a number")
    else:
        print('----- END -----')