def gen_compressed_data_file():
    big_table = dict()

    print("Get arrival time data")
    with open('METACENTRUM-2013-2.swf', 'r') as input_file:
        index = 0
        second_in_day = 60*60*24
        for line in input_file:
            # Ignore the comment lines
            if line[0] == ';':
                pass
            else:
                data = int(str.split(line)[1])%second_in_day
                if data in big_table:
                    big_table[data] += 1
                else:
                    big_table[data] = 1

    print("Save data to file")
    with open("arrival_time.txt", "w") as output_file:
        for key, val in big_table.iteritems():
            output_file.write(str(key) + " " + str(val) + "\n")

    print("File arrival_time.txt generated")

gen_compressed_data_file()
