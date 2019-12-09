def main():
    in_list = []
    new_list = []
    sort_list = []  # Sorting list store in this
    while True :
        input_in = input("Enter Elements :-")
        hold = int(input_in)
        in_list.append(hold)    # append User Numbers in list
    #   print("{} User List :-".format(in_list))       # if you want to see one by one list elements
        stop_exe = input("If you stop :")
        if stop_exe == 'stop':
            break
        else:                      # check the User Wish
            continue
    print("| {} | User List :-".format(in_list))

    for check in in_list:                          # check the Duplicate in list
        if check not in new_list:
            new_list.append(check)
    print("| {} |  List Without Duplicate Elements".format(new_list))
    check_length = len(new_list)
    # print("{} This is Length of List".format(check_length))    # if you want to see loop iterator values
    for check_outer in range(0 , check_length):
        for check_inner in range(0 , check_length):
            if new_list[check_outer] < new_list[check_inner]:        # apply condition on Loops
                store = new_list[check_outer]
                new_list[check_outer] = new_list[check_inner]
                new_list[check_inner] = store
                """"
                temp = new_list[check_inner]
                new_list[check_outer] = new_list[check_inner]
                new_list[check_inner] = temp """
    for result in range(0 , check_length):       # append values in new sort list
        value = new_list[result]
        sort_list.append(value)

    print("| {} | Sorting List in asscending Order  ".format(sort_list))             # print list

    """ x = str(value)
    convert = list(x)         # If you want to print one by one so execute this 3 lines 
    print(convert)"""
                                                                                           

if __name__ == "__main__":
    main()

