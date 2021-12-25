def validate_and_evaluate():
    try:

        user_input_num = int(user_element_dict["days"])
        if user_input_num > 0:
            calculate_hours = days_to_unit(user_input_num, user_element_dict["conversion_unit"])
            print(calculate_hours)
        elif user_input_num == 0:
            print(f"Please enter a number other than Zero")
        else:
            print("Please enter a positive number")

    except ValueError:
        print("Please enter a valid number")


user_input = input("Please enter the number of days and unit of conversion:\n")
user_elements = user_input.split(":")
user_element_dict = {"days": user_elements[0], "conversion_unit": user_elements[1]}
validate_and_evaluate()
