print('Welcome to my adventure game.')
choice = input('Do you wish to play this game? Type yes to continue playing: ').lower()

if choice != 'yes' :
    quit()
else :
    print('Thank you for choosing to play this game.')
    print('')
    print('You are caught in a land with a lot of hurdles, choose your choices carefully.')
    print('')
    print('1.Go right')
    print('2.Go left')
    print('3.Go back')

choice = int(input('Choose one of the choices above to continue playing: '))
if choice == 1 :
    print('There is a lion ahead')
    print('1.run')
    print('2.attack')

    choice_right = int(input('Choose one of the two choices: '))
    if choice_right == 1:
        print('Good idea')
        print('')
        print('1.Go right')
        print('2.Go left')
        print('3.Go back')

        choice_right2 =int(input('Choose one of the two choices: ')) 
        if choice_right2 == 1 :
            print('There is an intruder ahead')
            print('1.attack')
            print('2.wait for them to leave')

            pick = int(input('Pick one of the choices: '))
            if pick == 1 :
                print('Do you have weapons to attack them? ')
                print('1.Yes')
                print('2.No')

                pick2 = int(input('Pick one of the choices if you have a weapon or not: '))
                if pick2 == 1:
                    print('Go ahead and fight them.')
                    print('Sorry, the intruder has killed you.')
                    quit()
                elif pick2 == 2 :
                    print(' Thats too bad, Have you found somewhere to hide?')
                    print('1.Yes')
                    print('2.No')
                    pick3 = int(input('Pick if you have somewhere to hide or not'))
                    if pick3 == 1:
                        print('Good idea')

                        print('Would you like to go :')
                        print('1.right')
                        print('2.left')
                        print('3.back')
                        pick4 = int(input('Pick one of the choices above: '))
                        if pick4 == 1 :
                            print('There is a forest ahead, do you have a map to go through it?')
                            print('1.Yes')
                            print('2.No')
                            pick5 = int(input('Choose if you have a map or not: '))
                            if pick5 == 1 :
                                print('That is good, go ahead and cross the forest.')


                                print('You have come across a bear.')
                                print('Would you like to :')
                                print('1.Run')
                                print('2.Attack it')
                                pick6 = int(input('Please pick one of the choices above: '))
                                if pick6 == 1 :
                                    print('Congratulations! You have made it to the finish line!!')
                                elif pick6 == 2 :
                                    print('Sorry, the bear has killed you.')
                                    quit()
                                else:
                                    print('Please enter a valid choice.')


                            elif pick5 == 2 :
                                print('Sorry you have been stranded in the forest.')
                                quit()
                            else :
                                print('Please pick a valid choice')
                        

                    elif pick3 == 2 :
                        print('Sorry, the intruder has detected you and killed you.')
                        quit()
                    else:
                        print('Please put a valid choice.')

    elif choice_right == 2:
        print('Sorry, you have been killed by the lion')
        quit()
    else:
        print('Enter a valid choice.')

elif choice == 2:
    print('There is an ocean ahead, can you swim it through')
    print('1.yes')
    print('2.no')
    choice_left = int(input('Choose of the two options'))
    
    if choice_left == 1:
        print('You have made it to the other side')
        print('')
        print('You have encountered a monster')
        print('1.run')
        print('2.attack')
        left1 = int(input('Pick one of the choices above'))
        if left1 == 1 :
            print('That is a good idea')
            print('')
            print('Would you like to :')
            print('1.Go right')
            print('2.Go left')
            print('Go back')

            left2 =  int(input('Please pick one of the above choices'))
            if left2 ==  1:
                print('You have come across an ocean with crocodiles')
                print('')
                print('Would you like to :')
                print('1.Swim regardless')
                print('2.Look for an alternative route')
                left3 = int(input('Pick one of the above choices'))
                if left3 == 1 :
                    print('Sorry, the crocodiles have feasted on you.')
                    quit()
                elif left3 == 2 :
                    print('That is a good idea')
                    print('')
                else:
                    print('Please enter a valid choice')

                    print('1.There is a short route throught the desert and there is no food or water')
                    print('2.There is a long route in the sea')

                    left4 = int(input('Choose one of the two choices above'))
                    if left4 == 1:
                        print('You have died of hunger')
                        quit()
                    elif left4 == 2:
                        print('That is a good idea')

                    else:
                        print('Please pick a valid choice')
            elif left2 == 2 :
                print('There are a path full of snakes.')
                print('1.cross it')
                print('2.Look for another route')
                left5 = int(input('Pick one of the choices: '))
                if left5 == 1 :
                    print('Sorry the snakes have killed you.')
                    quit()
                if left5 == 2 :
                    print('You have come across a sleeping dragon.')
                    print('')
                    print('Would you like to :')
                    print('1.Slowly cross over the path.')
                    print('2.Go back or quit')
                    left6 = int(input('Choose one of these choices above: '))
                    if left6 == 1:
                        print('Congratulations! You have made it to the finish line!!')
                    if left6 == 2:
                        print('Sorry, Thats not a good idea but thanks for reaching this far')
                        quit()
                    else:
                        ('Please enter a valid choice')



        elif left1 == 2 :
            print('Sorry, you have been killed')
            quit()
        
        else :
            print('Please pick a valid choice.')

    elif choice_left ==2:
        print('Sorry, you cannot make it to the other side')
        quit()
    
    else:
        print('Please enter a valid option.')

elif choice == 3 :
    quit()