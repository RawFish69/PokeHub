def log_writer_A(list, point, levels):
    """This function is used to add data (captured pokemon, CP, etc) to the
    log file of each player. Call this function in the menu to access it"""
    with open('poke_track_log_A.txt', 'r') as reader:
        line_count = 0
        reader.readline()
        reader.readline()
        for line in reader:
            if line != '\n':
                line_count += 1
    with open('poke_track_log_A.txt', 'a+') as log:
        pokemon_count = line_count
        for i in range(len(list)):
            pokemon_count += 1
            log.write('{}. {}, '.format(pokemon_count, list[i]))
            log.write('{}, '.format(point[i]))
            log.write('{}\n'.format(levels[i]))
        return list, point, levels, pokemon_count


def log_writer_B(list, point, levels):
    """This function is used to add data (captured pokemon, CP, etc) to the
    log file of each player. Call this function in the menu to access it"""
    with open('poke_track_log_B.txt', 'r') as reader:
        line_count = 0
        reader.readline()
        reader.readline()
        for line in reader:
            if line != '\n':
                line_count += 1
    with open('poke_track_log_B.txt', 'a+') as log:
        pokemon_count = line_count
        for i in range(len(list)):
            pokemon_count += 1
            log.write('{}. {}, '.format(pokemon_count, list[i]))
            log.write('{}, '.format(point[i]))
            log.write('{}\n'.format(levels[i]))
        return list, point, levels, pokemon_count


def log_reader_A():
    """Reading from logs and displaying data line by line to the user.
    Call this function in the main menu to access it"""
    with open('poke_track_log_A.txt', 'r') as reader:
        reader.readline()
        reader.readline()
        for line in reader:
            section = line.strip()
            section = section.split(', ')
            the_name = section[0]
            the_cp = section[1]
            the_level = section[2]
            print('--------------------------------')
            print("Index & Name: {}".format(the_name))
            print("Current cp: {:.2f}".format(float(the_cp)))
            print("Current level: {}".format(the_level))
        print('--------------------------------')
        # for line in reader:
        #     print(line)


def log_reader_B():
    """Reading from logs and displaying data line by line to the user.
    Call this function in the main menu to access it"""
    with open('poke_track_log_B.txt', 'r') as reader:
        reader.readline()
        reader.readline()
        for line in reader:
            section = line.strip()
            section = section.split(', ')
            the_name = section[0]
            the_cp = section[1]
            the_level = section[2]
            print('--------------------------------')
            print("Index & Name: {}".format(the_name))
            print("Current cp: {:.2f}".format(float(the_cp)))
            print("Current level: {}".format(the_level))
        print('--------------------------------')
        # for line in reader:
        #     print(line)
