def battle(index_A, index_B, log_index_A, log_index_B):
    """Typing battle will start a battle between both players. To choose a pokemon,
    the appropriate player needs to choose a pokemon based on the
    index assigned in the poke_track_log.txt file. """
    global attack_type_1
    global attack_type_2
    global section_1, section_2, section_3, section_4
    global attack_base_A_1, attack_base_A_2, attack_base_A_3, attack_base_A_4
    global winner
    global crit
    section_1 = ''
    section_2 = ''
    section_3 = ''
    section_4 = ''
    index_A = int(index_A)
    index_B = int(index_B)
    Fainted = True
    winner = ''
    with open('poke_track_log_A.txt', 'r') as reader:
        reader.readline()
        reader.readline()
        for line in reader:
            if log_index_A in line[:3]:
                part = line.strip()
                part = part.split(', ')

                cp_A = float(part[1])
                level_A = int(part[2])
    with open('poke_track_log_B.txt', 'r') as reader:
        reader.readline()
        reader.readline()
        for line in reader:
            if log_index_B in line[:3]:
                part = line.strip()
                part = part.split(', ')

                cp_B = float(part[1])
                level_B = int(part[2])

    # type 1 is player B and type 2 is player A
    print('==================================================')
    print('')
    with open('pokemon_types.txt', 'r') as pokeattack_type:
        line_count = 0
        for line in pokeattack_type:
            line_count += 1
            if line_count == index_A:
                attack_type_2 = line
                print('Player A types: ', attack_type_2)
    with open('pokemon_types.txt', 'r') as pokeattack_type:
        line_count = 0
        for line in pokeattack_type:
            line_count += 1
            if line_count == index_B:
                attack_type_1 = line
                print('Player B types: ', attack_type_1)
    print('==================================================')
    name_A = poke_name(index_A)
    stats_A = poke_stats(name_A)

    name_B = poke_name(index_B)
    stats_B = poke_stats(name_B)

    Health_A = int(stats_A[2]) * math.sqrt(cp_A) * math.sqrt(level_A)
    Health_B = int(stats_B[2]) * math.sqrt(cp_B) * math.sqrt(level_B)

    Attack_A = int(stats_A[3]) * math.sqrt(cp_A)
    Attack_B = int(stats_B[3]) * math.sqrt(cp_B)
    Defense_A = int(stats_A[4]) * math.sqrt(cp_A)
    Defense_B = int(stats_B[4]) * math.sqrt(cp_B)
    Special_Attack_A = int(stats_A[5]) * math.sqrt(cp_A)
    Special_Attack_B = int(stats_B[5]) * math.sqrt(cp_B)
    Special_Defense_A = int(stats_A[6]) * math.sqrt(cp_A)
    Special_Defense_B = int(stats_B[6]) * math.sqrt(cp_B)
    Speed_A = int(stats_A[7]) * math.sqrt(cp_A)
    Speed_B = int(stats_B[7]) * math.sqrt(cp_B)


    print('Player A pokemon: {}'.format(name_A))
    print('Health: {:.2f}, Attack: {:.2f}, Defense: {:.2f}'.format(Health_A, Attack_A, Defense_A))
    print('Special Attack: {:.2f}, Special Defense: {:.2f}, Speed: {:.2f}'.format(Special_Attack_A, Special_Defense_A, Speed_A))
    print('--------------------------------------------------')

    print('Player B pokemon: {}'.format(name_B))
    print('Health: {:.2f}, Attack: {:.2f}, Defense: {:.2f}'.format(Health_B, Attack_B, Defense_B))
    print('Special Attack: {:.2f}, Special Defense: {:.2f}, Speed: {:.2f}'.format(Special_Attack_B, Special_Defense_B, Speed_B))
    print('==================================================')
    turn = 0
    if int(Speed_A) > int(Speed_B):
        print('Player A will go first')
        turn = 1
    elif int(Speed_B) > int(Speed_A):
        print('Player B will go first')
        turn = 2
    elif int(Speed_A) == int(Speed_B):
        print('Same, speed, randomize turn')
        turn = random.randint(1, 2)



    attack_type_2 = str(attack_type_2).strip()
    attack_type_2 = attack_type_2.split(', ')
    section_1 = attack_type_2[0]
    section_2 = attack_type_2[1]

    attack_type_1 = str(attack_type_1).strip()
    attack_type_1 = attack_type_1.split(', ')
    section_3 = attack_type_1[0]
    section_4 = attack_type_1[1]

    attack_base_A_1 = types(section_1, section_3)
    attack_base_A_2 = types(section_2, section_4)
    attack_base_B_1 = types(section_3, section_1)
    attack_base_B_2 = types(section_4, section_2)

    crit = False

    print('--------------------------------------------------')
    print('Battle Start!')

    while Fainted != False:
        try:
            if turn % 2 != 0:
                print('{}:'.format(name_A))
                print('| 1. Attack {}  | 2. Special Attack {} | 3. Attack Boost | 4. Defense Boost | 5. Escape | '.format(section_1, section_2))
                move_A = int(input('Choose your move (1, 2, 3, 4, 5): '))
                if move_A == 1:
                    if int(Defense_B) < int(Attack_A):
                        if random.randint(0, 100) <= 20:
                            crit = True
                        base_damage_A = (((int(Attack_A)) - (int(Defense_B))) * attack_base_A_1)
                        if crit:
                            base_damage_A *= 2
                            print('|Critical Hit, 2x Damage|')
                    else:
                        if random.randint(0, 100) <= 20:
                            crit = True
                        base_damage_A = 50 * attack_base_A_1
                        if crit:
                            base_damage_A *= 2
                            print('|Critical Hit, 2x Damage|')
                    Health_B = Health_B - base_damage_A
                    if Health_B > 0:
                        print('{} did {:.2f} damage to {}'.format(name_A, base_damage_A, name_B))
                        print('{} has {:.2f} Health remaining'.format(name_B, Health_B))
                    else:
                        print('{} did {:.2f} damage to {}'.format(name_A, base_damage_A, name_B))
                        print('{} has 0 Health remaining...'.format(name_B))
                        winner = 'A'
                    turn += 1
                    crit = False
                if move_A == 2:
                    if int(Special_Defense_B) < int(Special_Attack_A):
                        if random.randint(0, 100) <= 20:
                            crit = True
                        special_damage_A = (((int(Special_Attack_A)) - (int(Special_Defense_B))) * attack_base_A_2)
                        if crit:
                            special_damage_A *= 2
                            print('|Critical Hit, 2x Damage|')
                    else:
                        if random.randint(0, 100) <= 20:
                            crit = True
                        special_damage_A = 50 * attack_base_A_2
                        if crit:
                            special_damage_A *= 2
                            print('|Critical Hit, 2x Damage|')
                    Health_B = Health_B - special_damage_A
                    if Health_B > 0:
                        print('{} did {:.2f} special damage to {}'.format(name_A, special_damage_A, name_B))
                        print('{} has {:.2f} Health remaining'.format(name_B, Health_B))
                    else:
                        print('{} did {:.2f} damage to {}'.format(name_A, special_damage_A, name_B))
                        print('{} has 0 Health remaining...'.format(name_B))
                        winner = 'A'
                    turn += 1
                    crit = False
                if move_A == 3:
                    Attack_A *= 1.05
                    Special_Attack_A *= 1.05
                    print('{} received an attack boost.'.format(name_A))
                    print('Current Stats: ')
                    print("Attack: {:.2f}, Special Attack: {:.2f}".format(Attack_A, Special_Attack_A))
                    turn += 1
                if move_A == 4:
                    Defense_A *= 1.05
                    Special_Defense_A *= 1.05
                    print('{} received a defense boost.'.format(name_A))
                    print('Current Stats: ')
                    print("Defense: {:.2f}, Special Defense: {:.2f}".format(Defense_A, Special_Defense_A))
                    turn += 1
                elif move_A == 5:
                    Health_A = 0
                    print('You escaped')
                    winner = 'B'
            elif turn % 2 == 0:
                print('{}:'.format(name_B))
                print('| 1. Attack {}  | 2. Special Attack {} | 3. Attack Boost | 4. Defense Boost | 5. Escape | '.format(section_1, section_2))
                move_B = int(input('Choose your move (1, 2, 3, 4, 5): '))
                if move_B == 1:
                    if int(Defense_A) < int(Attack_B):
                        if random.randint(0, 100) <= 20:
                            crit = True
                        base_damage_B = (((int(Attack_B)) - (int(Defense_A))) * attack_base_B_1)
                        if crit:
                            base_damage_B *= 2
                            print('|Critical Hit, 2x Damage|')
                    else:
                        if random.randint(0, 100) <= 20:
                            crit = True
                        base_damage_B = 50 * attack_base_B_1
                        if crit:
                            base_damage_B *= 2
                            print('|Critical Hit, 2x Damage|')
                    Health_A = Health_A - base_damage_B
                    if Health_A > 0:
                        print('{} did {:.2f} damage to {}'.format(name_B, base_damage_B, name_A))
                        print('{} has {:.2f} Health remaining'.format(name_A, Health_A))
                    else:
                        print('{} did {:.2f} damage to {}'.format(name_B, base_damage_B, name_A))
                        print('{} has 0 Health remaining...'.format(name_A))
                        winner = 'B'
                    turn += 1
                    crit = False
                if move_B == 2:
                    if int(Special_Defense_A) < int(Special_Attack_B):
                        if random.randint(0, 100) <= 20:
                            crit = True
                        special_damage_B = (((int(Special_Attack_B)) - (int(Special_Defense_A))) * attack_base_B_2)
                        if crit:
                            special_damage_B *= 2
                            print('|Critical Hit, 2x Damage|')
                    else:
                        if random.randint(0, 100) <= 20:
                            crit = True
                        special_damage_B = 50 * attack_base_B_2
                        if crit:
                            special_damage_B *= 2
                            print('|Critical Hit, 2x Damage|')
                    Health_A = Health_A - special_damage_B
                    if Health_A > 0:
                        print('{} did {:.2f} damage to {}'.format(name_B, special_damage_B, name_A))
                        print('{} has {:.2f} Health remaining'.format(name_A, Health_A))
                    else:
                        print('{} did {:.2f} damage to {}'.format(name_B, special_damage_B, name_A))
                        print('{} has 0 Health remaining...'.format(name_A))
                        winner = 'B'
                    turn += 1
                    crit = False
                if move_B == 3:
                    Attack_B *= 1.05
                    Special_Attack_A *= 1.05
                    print('{} received an attack boost.'.format(name_B))
                    print('Current Stats: ')
                    print("Attack: {:.2f}, Special Attack: {:.2f}".format(Attack_B, Special_Attack_B))
                    turn += 1
                if move_B == 4:
                    Defense_B *= 1.05
                    Special_Defense_B *= 1.05
                    print('{} received a defense boost.'.format(name_B))
                    print('Current Stats: ')
                    print("Defense: {:.2f}, Special Defense: {:.2f}".format(Defense_B, Special_Defense_B))
                    turn += 1
                elif move_B == 5:
                    Health_B = 0
                    print('You escaped')
                    winner = 'A'
            if Health_A <= 0 or Health_B <= 0:
                Fainted = False
        except:
            print("Input should only be Integer!")
    if Health_A > Health_B:
        print("Player A won!")
    elif Health_B > Health_A:
        print("Player B won!")
    else:
        print("It's a draw")
    if winner == 'A':
        with open('candy_A.txt', 'r') as reward:
            candy_count = int(reward.readline())
        candy_count += 10
        print('Reward has been assigned to player A!')
        with open('candy_A.txt', 'w') as reward:
            reward.write(str(candy_count))
        print('[Candy + 10]')
    elif winner == 'B':
        with open('candy_B.txt', 'r') as reward:
            candy_count = int(reward.readline())
        candy_count += 10
        print('Reward has been assigned to player B!')
        with open('candy_B.txt', 'w') as reward:
            reward.write(str(candy_count))
        print('[Candy + 10]')
