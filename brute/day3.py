def check_for_indicator(astr, indicator):
    if astr == indicator:
        return True
    else:
        return False


def validate_if_string_is_number(astr):
    try:    
        number = int(astr)
        return number
    except ValueError:
        return False


def get_number(blob, blob_index, digit_placeholder):
    numbers = ""
    while True:
        response = validate_if_string_is_number(blob[blob_index])     
        if response is not False:
            blob_index += 1
            numbers += str(response)
        else:
            if digit_placeholder == "first":
                comma_validate = check_for_indicator(blob[blob_index], ",")
                if comma_validate is True:
                    blob_index +=1
                    return numbers, blob_index
                else:
                    blob_index += 1
                    numbers = ""
                    break
            if digit_placeholder == "second":
                smallblackclose_validate = check_for_indicator(blob[blob_index], ")")
                if smallblackclose_validate is True:
                    blob_index +=1
                    return numbers, blob_index
                else:
                    blob_index += 1
                    numbers = ""
                    break
    return numbers, blob_index
        
        
def parse_string(blob):
    i = 0
    numbers_to_add = 0
    found_mul = 0
    while i <= len(blob)-1:
        starter_string = blob[i]
        if starter_string == "m":
           if i+4 < len(blob)-1:
              compare_string = f"{blob[i]}{blob[i+1]}{blob[i+2]}{blob[i+3]}"
              if compare_string == "mul(":
                found_mul = found_mul +  1
                i = i + 4
                number_to_add, new_index = get_number(blob, i, "first")
                if number_to_add != "":
                    second_number_to_add, second_index = get_number(blob, new_index, "second")
                    if second_number_to_add != "":
                        multiplied_value = int(number_to_add)* int(second_number_to_add)
                        numbers_to_add += multiplied_value
        i = i+1
    return numbers_to_add
   

def main():
    with open("day3_input.txt", "r") as f:
        data = f.read()
    parse_to_find_two_numbers = parse_string(data)  
    print(parse_to_find_two_numbers)
    
main()
