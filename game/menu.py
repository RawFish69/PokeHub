def poke():
    """Main function of poke log generator, user can store new find,
    check stored finds, check info, and overwrite the current log"""
    global stats
    global the_name_A, the_name_B, the_name
    global log_index_A, log_index_B
    pokemon_list = []
    combat_point = []
    level = []
    battle_list = []
    turn = 1
    print('-----------------------------------------')
    print('If this is your first time playing,')
    print('Enter [create] to generate player files')
    print('-----------------------------------------')
    print('Enter [catch] to catch a pokemon')
    print('Enter [search] to search pokemon\'s stats')
    print('Enter [level] to level up pokemon ')
    print('Enter [battle] to Battle')
    print('Enter [create] to generate a log file')
    print('Enter [update] to update log manually')
    print('Enter [skip] to skip your turn')
    print('Enter [view] to view log file')
    print('Enter [End] to End program')
    print('Enter [help] to view command list')
    print('-----------------------------------------')
    cmd = str(input('Enter any key to continue, [End] to End program: '))
    while cmd not in ('End', 'end'):
        cmd = str(input('Enter command: '))
        if cmd in ('Catch', 'catch'):
            if turn % 2 != 0:
                ID = 'A'
                print('Player A, It\'s your turn.')
                captured = catch(ID)
                stats = poke_stats(captured)
                pokemon_list.append(stats[1])
                lvl = random.randint(1, 3)
                level.append(lvl)
                cp_min = float(get_cp(stats[0])[0])
                cp_max = float(get_cp(stats[0])[1])
                current_cp = cp_min + (cp_min * 0.0093 / ((0.094 * math.sqrt(lvl))))
                combat_point.append(current_cp)
                if current_cp >= cp_max:
                    print('{} has reached the maximum cp {}'.format(stats[1], cp_max))
                updater = log_writer_A(pokemon_list, combat_point, level)
                pokemon_list = []
                combat_point = []
                level = []
                print('Log file has been updated.')
                turn += 1
                print('...Switching turns...')
            elif turn % 2 == 0:
                ID = 'B'
                print('Player B, It\'s your turn.')
                captured = catch(ID)
                stats = poke_stats(captured)
                pokemon_list.append(stats[1])
                lvl = random.randint(1, 3)
                level.append(lvl)
                cp_min = float(get_cp(stats[0])[0])
                cp_max = float(get_cp(stats[0])[1])
                current_cp = cp_min + (cp_min * 0.0093 / ((0.094 * math.sqrt(lvl))))
                combat_point.append(current_cp)
                if current_cp >= cp_max:
                    print('{} has reached the maximum cp {}'.format(stats[1], cp_max))
                updater = log_writer_B(pokemon_list, combat_point, level)
                pokemon_list = []
                combat_point = []
                level = []
                print('Log file has been updated.')
                turn += 1
                print('...Switching turns...')
        elif cmd in ('Search', 'search'):
            if turn % 2 != 0:
                print('Player A')
                pick_name = str(input('The name of pokemon: '))
                stats = poke_stats(pick_name)
                print('---------------------pokemon stats---------------------')
                print('Pokemon name: {}, Index: {}'.format(stats[1], stats[0]))
                print('Minimum CP: {}, Maximum CP: {}'.format(stats[8], stats[9]))
                print('Health: {}, Attack: {}, Defense: {}'.format(stats[2], stats[3], stats[4]))
                print('Special Attack: {}, Special Defense: {}, Speed: {}'.format(stats[5], stats[6], stats[7]))
                print('-------------------------------------------------------')
            elif turn % 2 == 0:
                print('Player B')
                pick_name = str(input('The name of pokemon: '))
                stats = poke_stats(pick_name)
                print('---------------------pokemon stats---------------------')
                print('Pokemon name: {}, Index: {}'.format(stats[1], stats[0]))
                print('Minimum CP: {}, Maximum CP: {}'.format(stats[8], stats[9]))
                print('Health: {}, Attack: {}, Defense: {}'.format(stats[2], stats[3], stats[4]))
                print('Special Attack: {}, Special Defense: {}, Speed: {}'.format(stats[5], stats[6], stats[7]))
                print('-------------------------------------------------------')
        elif cmd in ('Battle', 'battle'):
            if len(battle_list) == 0:
                log_index_A = input('Player A, choose your pokemon: ')
                with open('poke_track_log_A.txt', 'r') as reader:
                    reader.readline()
                    reader.readline()
                    for line in reader:
                        if log_index_A in line[:3]:
                            section = line.strip()
                            section = section.split(', ')
                            the_name = section[0]
                    the_name = the_name.split('. ')
                    name_A = the_name[1]
                index_A = poke_stats(name_A)[0]
                battle_list.append(index_A)
            if len(battle_list) == 1:
                log_index_B = input('Player B, choose your pokemon: ')
                with open('poke_track_log_B.txt', 'r') as reader:
                    reader.readline()
                    reader.readline()
                    for line in reader:
                        if log_index_B in line[:3]:
                            section = line.strip()
                            section = section.split(', ')
                            the_name = section[0]
                    the_name = the_name.split('. ')
                    name_B = the_name[1]
                index_B = poke_stats(name_B)[0]
                battle_list.append(index_B)
            if len(battle_list) >= 2:
                battle(battle_list[0], battle_list[1], log_index_A, log_index_B)
            battle_list = []
            turn += 1
            print('...Switching turns...')
        elif cmd in ('Level', 'level'):
            if turn % 2 != 0:
                print('Player A, It\'s your turn.')
                pick_pokemon = input('Enter the index of pokemon: ')
                try:
                    if int(pick_pokemon):
                        lvling = leveling_A(pick_pokemon)
                        turn += 1
                        print('...Switching turns...')
                    else:
                        print('Please enter valid index')
                except:
                    print('Please enter valid input')
            elif turn % 2 == 0:
                print('Player B, It\'s your turn.')
                pick_pokemon = input('Enter the index of pokemon: ')
                try:
                    if int(pick_pokemon) < 10:
                        lvling = leveling_B(pick_pokemon)
                        turn += 1
                        print('...Switching turns...')
                    else:
                        print('Please enter valid index')
                except:
                    print('Please enter valid input')
        elif cmd in ('Create', 'create'):
            log_file = log_generator(pokemon_list, combat_point, level)
            print('Log file successfully generated.')
            cmd = 'End'
        elif cmd in ('Update', 'update'):
            if turn % 2 != 0:
                append_file = log_writer_A(pokemon_list, combat_point, level)
                pokemon_list = []
                combat_point = []
                level = []
                print('Log file updated.')
            elif turn % 2 == 0:
                append_file = log_writer_B(pokemon_list, combat_point, level)
                pokemon_list = []
                combat_point = []
                level = []
                print('Log file updated.')
        elif cmd in ('Skip', 'skip'):
            print('You have skipped this round.')
            turn += 1
        elif cmd in ('View', 'view'):
            if turn % 2 != 0:
                print('Player A:')
                view_file = log_reader_A()
            elif turn % 2 == 0:
                print('Player B:')
                view_file = log_reader_B()
        elif cmd in ('Help', 'help'):
            help_cmd = help()
        elif cmd in ('End', 'end'):
            print('Program Ended, exiting right now.')
            return pokemon_list, combat_point, level
