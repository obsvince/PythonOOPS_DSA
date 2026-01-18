def reverse_with_list_comprehension(string):
    return string[::-1]

def reverse_with_loop(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string

    return reversed_string



if __name__ == '__main__':
    string_to_reverse = "hello world"
    print(reverse_with_list_comprehension(string_to_reverse))
    print(reverse_with_loop(string_to_reverse))
