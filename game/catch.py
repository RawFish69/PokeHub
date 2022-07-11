def catch(ID):
    """Gotta catch one of em."""
    global pokemon_captured
    index_rolled = random.randint(1, 151)
    print('A wild {} appears!'.format(poke_name(index_rolled)))
    # capture = input('Bypass capture mini game? (T/F):')
    capture = game()
    if capture in ('T', 't'):
        pokemon_captured = poke_name(index_rolled)
        print('A {} has been captured!'.format(pokemon_captured))
        if ID == 'A':
            with open('candy_A.txt', 'r') as candy_A:
                candy = int(candy_A.readline())
                candy = candy + 5
            with open('candy_A.txt', 'w') as candy_A:
                candy_A.write(str(candy))
        if ID == 'B':
            with open('candy_B.txt', 'r') as candy_B:
                candy = int(candy_B.readline())
                candy = candy + 5
            with open('candy_B.txt', 'w') as candy_B:
                candy_B.write(str(candy))
        print('Reward candies have been assigned!')
    else:
        pokemon_captured = poke_name(index_rolled)
        print('A {} has been captured!'.format(pokemon_captured))
    return pokemon_captured
