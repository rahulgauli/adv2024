def get_distance(left: list, right: list):
    i =0 
    j =0
    to_sum = []
    while i <= len(left)-1 and j <= len(right)-1:
        distance = left[i] - right[j]
        distance = abs(distance)
        to_sum.append(distance)
        i += 1
        j +=1
    distance_sum = 0
    for anumber in to_sum:
        distance_sum += anumber
    return distance_sum

def get_similarity(left: list, right: list):
    to_sum = []
    for a_number in left:
        number_of_occurences = 0 
        for another_number in right:
            if another_number == a_number:
                print(f"found one for{a_number} with {another_number}")
                number_of_occurences += 1
        to_sum_num = a_number * number_of_occurences
        to_sum.append(to_sum_num)
    distance_sum = 0
    for anumber in to_sum:
        distance_sum += anumber
    return distance_sum

def get_two_lists(data: str):
    left = []
    right = []
    data = data.split("\n")
    for a_pair in data:
        new_pair = a_pair.split("   ")
        left.append(int(new_pair[0]))
        right.append(int(new_pair[1]))
    return left, right

def main():
    with open("day1input.txt", "r") as f:
        data = f.read()
    left, right = get_two_lists(data)
    left.sort()
    right.sort()
    # print(left, right)
    list_of_differences = get_distance(left,right)
    similarity = get_similarity(left, right)
    print(list_of_differences)
    print(similarity)

main()

