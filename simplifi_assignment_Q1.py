def convert_to_indian_currency(num):
    num_str = str(num)
    
    n = len(num_str)
    result = ""
    for i in range(n):
        result += num_str[i]
        pos = n - i - 1
        if pos > 0 and pos % 2 == 0 and pos > 2:
            result += ","
        elif pos == 3:
            result += ","
    return result


num = int(input("Enter integer value: "))

formatted_num = convert_to_indian_currency(num)
print(formatted_num)
