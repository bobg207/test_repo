file = "file_name.txt"
with open(file, 'r') as temp:
    data = temp.read()  # .read() returns all data as one string
    print(data)

    # data_line = temp.readline()
    # print(data_line)

    # data_list = temp.readlines() # return a list with each line 
    # print(data_list)             # as a string

split_data = data.split()
print(split_data)