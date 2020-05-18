def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for elements in range(list_length):
        try:
            quotient = my_list_1[elements] / my_list_2[elements]
        except ZeroDivisionError:   # If any error occurs reset quo to 0
            print("division by 0")  # to avoid last saved quotient errors
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        except TypeError:
            print("wrong type")
            quotient = 0
        finally:
            result_list.append(quotient)

    return result_list
