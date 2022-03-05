# initialize user interface
main_name = input("Enter your name: ")
print(f'Welcome to {main_name.title()}\'s Address Book!')

# populate a dictionary
add_book = {'karen longstreet': ['12 Boulevard, Canada', ['07087145533', '08040050067'], ['karen@gmail.com']],
            'logan moore': ['Block B, 14th street, New York', ['08171771744'], ['logan@golmach.com']],
            'jay pritchett': ['4 Loft K, The Louvre, London', ['08024505034'], ['jay@hotmail.com', 'jayson@bing.com']],
            'ron swanson': ['Crust Building, 7th Floor, Eagleton-Pawnee', ['09078785211'],
                             ['ron@yahoo.com', 'ronny@sidtech.com', 'ron.sw@stfu.net', 'r.swan@gmail.com']],
            'gloria david': ['11B Sunday Avenue, Montreal', ['03056711364', '09130020055', '07133355522'],
                             ['gloria@bing.com', 'g.esta@llc.net']]}

# main program loop
while True:
    # user options (available actions in address book)
    option = input('\n[a] - add a new contact'
                   '\n[e] - edit a contact' 
                   '\n[d] - delete a contact'
                   '\n[s] - search for a contact' 
                   '\n[v] - view all contacts'
                   '\n[x] - exit'
                   '\nEnter option: ')

    # MAIN OPTION a. add new contact
    if option == 'a':
        print('\nAdding New Contact')
        name = input('Enter contact name: ').lower()
        if name in add_book:
            print('Contact already exists!')
        else:
            add = input('Enter address: ')
            phone = []
            email = []
            print('Enter phone number(s)...Enter 1 to stop')
            a = 1
            while True:
                phone_num = (input(f'Enter phone number {a}: '))
                if phone_num == '1':
                    break
                phone.append(phone_num)
                a += 1

            print('Enter email address(es)...Enter 1 to stop')
            b = 1
            while True:
                email_add = input(f'Enter email address {b}: ')
                if email_add == '1':
                    break
                email.append(email_add)
                b += 1
            add_book[name] = [add, phone, email]
            print(f'\n{name.title()} has been added to your contacts.')
            print(f'Address: {add_book[name][0]}')
            print('Phone Number(s): ', end=' ')
            print(*add_book[name][1], sep=', ')
            print('E-mail Address(es): ', end=' ')
            print(*add_book[name][2], sep=', ')

    # MAIN OPTION e. edit a contact
    elif option == 'e':
        print("\nEditing Contact")
        edit = input('Enter the name of the contact you want to edit: ').lower()

        if edit in add_book:
            print(f'Name: {edit.title()}\nAddress: {add_book[edit][0]}')
            print('Phone Number(s): ', end=' ')
            print(*add_book[edit][1], sep=', ')
            print('E-mail Address(es): ', end=' ')
            print(*add_book[edit][2], sep=', ')
            while True:
                edit_option = input('\n[1] - Change Contact Name'
                                    '\n[2] - Change Address' 
                                    '\n[3] - Change Phone Number'
                                    '\n[4] - Change Email' 
                                    '\n[#] - Previous menu'
                                    '\nEnter option: ')

                # change contact name
                if edit_option == '1':
                    new_name = input('Enter New name: ').lower()
                    temp = add_book[edit]  # moving the dictionary object into a temporary variable
                    temp_name = edit  # copy the old name to a variable
                    del add_book[edit]  # delete object from dictionary
                    add_book[new_name] = temp  # create a new key-value pair from temporary variables
                    # edit = new_name
                    print(f'>>{temp_name.title()} has been updated to {new_name.title()}')

                # change contact address
                elif edit_option == '2':
                    new_add = input(f'Enter new address for {edit.title()}: ')
                    add_book[edit][0] = new_add
                    print(f'>>{edit.title()}\'s address has been updated.')

                # change contact phone number
                elif edit_option == '3':
                    while True:
                        phone_edit = input('\n[1] - Add New Phone No'
                                           '\n[2] - Edit Current Phone No' 
                                           '\n[3] - Delete a phone number'
                                           '\n[#] - previous menu'
                                           '\nEnter option: ')

                        # add new phone number
                        if phone_edit == '1':
                            cur_cnt = len(add_book[edit][1]) + 1
                            phone_no = input(f'Enter phone no {cur_cnt}: ')
                            add_book[edit][1].append(phone_no)
                            print(f'>>{edit.title()}\'s phone number has been updated.')

                        # edit existing phone number
                        elif phone_edit == '2':
                            for i in range(len(add_book[edit][1])):
                                print(f'\n[{(i + 1)}] - {add_book[edit][1][i]}')
                            choice = int(input('Enter option: '))
                            index = choice - 1
                            new_phone_no = input(f'Enter new phone no: ')
                            add_book[edit][1][index] = new_phone_no
                            print(f'>>{edit.title()}\'s phone number has been updated.')

                        # delete existing phone number
                        elif phone_edit == '3':
                            for i in range(len(add_book[edit][1])):
                                print(f'[{(i + 1)}] - {add_book[edit][1][i]}')
                            choice = int(input('Enter option: '))
                            index = choice - 1
                            del add_book[edit][1][index]
                            print(f'>>Phone number {choice} has been deleted successfully.')

                        # exit phone number edit option
                        elif phone_edit == '#':
                            break

                        else:
                            print(f'Invalid Entry, {main_name.title()}')

                # change contact email
                elif edit_option == '4':
                    while True:
                        email_edit = input('\n[1] - Add New Email'
                                           '\n[2] - Edit Existing Email' 
                                           '\n[3] - Delete an Email'
                                           '\n[#] - previous menu'
                                           '\nEnter option: ')

                        # add a new email address
                        if email_edit == '1':
                            e_cnt = len(add_book[edit][2]) + 1
                            e_mail = input(f'Enter Email {e_cnt}: ')
                            add_book[edit][2].append(e_mail)
                            print(f'>>{edit.title()}\'s Email Address has been updated.')

                        # edit existing email address
                        elif email_edit == '2':
                            for i in range(len(add_book[edit][2])):
                                print(f'[{(i + 1)}] - {add_book[edit][2][i]}')
                            choice = int(input('Enter option: '))
                            index = choice - 1
                            new_email = input(f'Enter new Email address: ')
                            add_book[edit][2][index] = new_email
                            print(f'>>{edit.title()}\'s Email Address has been updated.')

                        # delete existing email address
                        elif email_edit == '3':
                            for i in range(len(add_book[edit][2])):
                                print(f'[{(i + 1)}] - {add_book[edit][2][i]}')
                            choice = int(input('Enter option: '))
                            index = choice - 1
                            del add_book[edit][2][index]
                            print(f'>>Email address {choice} has been deleted successfully.')

                        # exit email edit option
                        elif email_edit == '#':
                            break

                        else:
                            print(f'Invalid Entry, {main_name.title()}')

                # exit edit options. Return to main options
                elif edit_option == '#':
                    break
                else:
                    print(f'Invalid option, {main_name.title()}')

        else:
            print(f'{edit} not found!')

    # MAIN OPTION d. delete a contact
    elif option == 'd':
        print("\nDelete Existing Contact")
        delete = input('Enter the name of the contact you want to delete: ').lower()
        if delete in add_book:
            print(f'Name: {delete.title()}\nAddress: {add_book[delete][0]}')
            print('Phone Number(s): ', end=' ')
            print(*add_book[delete][1], sep=', ')
            print('E-mail Address(es): ', end=' ')
            print(*add_book[delete][2], sep=', ')
            while True:
                del_option = input('\n[1] - CANCEL'
                                   '\n[ENTER] key - DELETE contact'
                                   '\nEnter option: ')
                if del_option == '':
                    del add_book[delete]
                    print(f'>>{delete.title()} has been removed from your contacts.')
                    break
                elif del_option == '1':
                    print('>>Deletion process terminated...')
                    break

                else:
                    print(f'Invalid option, {main_name.title()}')
        else:
            print(f'{delete.title()} not found!')

    # MAIN OPTION s. search for a contact
    elif option == 's':
        print("\nView Details of Existing Contact")
        while True:
            search = input('Enter contact name: ')
            if search in add_book:
                print(f"Contact Name: {search.title()}\nAddress: {add_book[search][0]}")
                for phone_no in range(len(add_book[search][1])):
                    print(f'Phone Number {(phone_no + 1)}: {add_book[search][1][phone_no]}')
                for mail in range(len(add_book[search][2])):
                    print(f'Email {(mail + 1)}: {add_book[search][2][mail]}')
                break
            else:
                print(f"{search} not found!")
                break

    # MAIN OPTION v. view all contacts
    elif option == 'v':
        print(f"\nHere is a list of all contacts, {main_name.title()}")
        for i in add_book:
            print(f"Contact Name: {i.title()}\nAddress: {add_book[i][0]}")
            print('Phone Number(s): ', end=' ')
            print(*add_book[i][1], sep=', ')
            print('E-mail Address(es): ', end=' ')
            print(*add_book[i][2], sep=', ')
            print()

    # MAIN OPTION x. Exit program
    elif option == 'x':
        print(f"\nBye Bye, {main_name.title()}...")
        break

    else:
        print(f'Invalid operation, {main_name.title()}')
