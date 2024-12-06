        
def get_direction(_change: int):
    if _change>0:
        return 1
    return -1

def create_new_list(original_list, index):
    new_list = []

    for item_index, item_ in enumerate(original_list):  
        if item_index != index:
            new_list.append(item_)
    return new_list

def check_safety(input: list):
    i = 1
    valid_changes = [1,2,3,-1,-2,-3]
    initial_value = input[0]
    _change = None
    _direction = None
    while i<len(input):
        if _change is None and _direction is None:
            _change = initial_value - input[i]
            initial_value = input[i]
            i = i + 1
            if _change not in valid_changes:
                return False
            _direction = get_direction(_change)
        apparent_change = initial_value - input[i]
        ongoing_direction  = get_direction(apparent_change)
        if ongoing_direction != _direction or apparent_change not in valid_changes:
            return False
        initial_value = input[i]
        i = i + 1
    return True


def validate_input(input: list[list]):
    output= []
    for a_input in input:
        stn_safety = check_safety(a_input)
        if stn_safety is True:    
            output.append({"safety":stn_safety, "input": a_input})
        else:
            index = 0
            print("initially we got a false")
            while index <= len(a_input)-1:
                new_list = create_new_list(a_input, index)
                new_result = check_safety(new_list)
                print(new_result, new_list)
                if new_result is True:
                    print("how many times are we here")
                    output.append({"safety":new_result, "input": a_input})
                    break
                index += 1
    return output


def main(input:str):
    to_validate = [ ]
    input = input.split("\n")
    for a_input in input:
        new_input = a_input.split(" ")
        new_input = [ int(a_num) for a_num in new_input]
        to_validate.append(new_input)
    return validate_input(to_validate)


with open("input.txt", "r") as f:
    data = f.read()
    result = main(data)
    # print(result)
    true = 0
    for a_output in result:
        if a_output["safety"] is True:
            true = true + 1
    print(true)