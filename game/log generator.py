def log_generator(list, point, levels):
    """This function will generate a log to a specific player with the pokemons
    that they've captured, including name, CP, and level assigned."""
    with open('poke_track_log_A.txt', 'w') as log:
        pokemon_count = 0
        log.write('player_ID: {}\n'.format('A'))
        log.write('Current pokemons: \n')
        for i in range(len(list)):
            pokemon_count += 1
            log.write('{}. {}, '.format(pokemon_count, list[i]))
            log.write('{}, '.format(point[i]))
            log.write('{}\n'.format(levels[i]))
    with open('poke_track_log_B.txt', 'w') as log:
        pokemon_count = 0
        log.write('player_ID: {}\n'.format('B'))
        log.write('Current pokemons: \n')
        for i in range(len(list)):
            pokemon_count += 1
            log.write('{}. {}, '.format(pokemon_count, list[i]))
            log.write('{}, '.format(point[i]))
            log.write('{}\n'.format(levels[i]))

    with open('candy_A.txt', 'w') as candy_A:
        candy_A.write('0')
    with open('candy_B.txt', 'w') as candy_B:
        candy_B.write('0')
