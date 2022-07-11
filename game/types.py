def types(attack_type, attack_type_1):
    """This function has all the types that damage calculation needs
    it determines type match ups"""
    global attack_base
    attack_base = 1
    if 'Water' in attack_type_1:
        if attack_type == 'Electric':
            attack_base += 1
        if attack_type == 'Grass':
            attack_base += 1
        if attack_type == 'Fire':
            attack_base -= .5
        if attack_type == 'Water':
            attack_base -= .5
        if attack_type == 'Ice':
            attack_base -= .5
        if attack_type == 'Steel':
            attack_base -= .5
    if 'Normal' in attack_type_1:
        if attack_type == 'Fighting':
            attack_base += 1
        if attack_type == 'Ghost':
            attack_base = 0
    if 'Fire' in attack_type_1:
        if attack_type == 'Fire':
            attack_base -= .5
        if attack_type == 'Water':
            attack_base += 1
        if attack_type == 'Grass':
            attack_base -= .5
        if attack_type == 'Ice':
            attack_base -= .5
        if attack_type == 'Ground':
            attack_base += 1
        if attack_type == 'Bug':
            attack_base -= .5
        if attack_type == 'Rock':
            attack_base += 1
        if attack_type == 'Steel':
            attack_base -= .5
        if attack_type == 'Fairy':
            attack_base -= .5
    if 'Electric' in attack_type_1:
        if attack_type == 'Electric':
            attack_base -= .5
        if attack_type == 'Ground':
            attack_base += 1
        if attack_type == 'Flying':
            attack_base -= .5
        if attack_type == 'Steel':
            attack_base -= .5
    if 'Grass' in attack_type_1:
        if attack_type == 'Fire':
            attack_base += 1
        if attack_type == 'Water':
            attack_base -= .5
        if attack_type == 'Electric':
            attack_base -= .5
        if attack_type == 'Grass':
            attack_base -= .5
        if attack_type == 'Ice':
            attack_base += 1
        if attack_type == 'Poison':
            attack_base += 1
        if attack_type == 'Ground':
            attack_base -= .5
        if attack_type == 'Flying':
            attack_base += 1
        if attack_type == 'Bug':
            attack_base += 1
    if 'Ice' in attack_type_1:
        if attack_type == 'Fire':
            attack_base += 1
        if attack_type == 'Ice':
            attack_base -= .5
        if attack_type == 'Fighting':
            attack_base += 1
        if attack_type == 'Rock':
            attack_base += 1
        if attack_type == 'Steel':
            attack_base += 1
    if 'Fighting' in attack_type_1:
        if attack_type == 'Flying':
            attack_base += 1
        if attack_type == 'Psychic':
            attack_base += 1
        if attack_type == 'Bug':
            attack_base -= .5
        if attack_type == 'Rock':
            attack_base -= .5
        if attack_type == 'Dark':
            attack_base -= .5
        if attack_type == 'Fairy':
            attack_base += 1
    if 'Poison' in attack_type_1:
        if attack_type == 'Grass':
            attack_base -= .5
        if attack_type == 'Fighting':
            attack_base -= .5
        if attack_type == 'Poison':
            attack_base -= .5
        if attack_type == 'Ground':
            attack_base += 1
        if attack_type == 'Psychic':
            attack_base += 1
        if attack_type == 'Bug':
            attack_base -= .5
        if attack_type == 'Fairy':
            attack_base -= .5
    if 'Ground' in attack_type_1:
        if attack_type == 'Water':
            attack_base += 1
        if attack_type == 'Electric':
            attack_base = 0
        if attack_type == 'Grass':
            attack_base += 1
        if attack_type == 'Ice':
            attack_base += 1
        if attack_type == 'Poison':
            attack_base -= .5
        if attack_type == 'Rock':
            attack_base -= .5
    if 'Flying' in attack_type_1:
        if attack_type == 'Electric':
            attack_base += 1
        if attack_type == 'Grass':
            attack_base -= .5
        if attack_type == 'Ice':
            attack_base += 1
        if attack_type == 'Fighting':
            attack_base -= .5
        if attack_type == 'Ground':
            attack_base = 0
        if attack_type == 'Bug':
            attack_base -= .5
        if attack_type == 'Rock':
            attack_base += 1
    if 'Psychic' in attack_type_1:
        if attack_type == 'Fighting':
            attack_base -= .5
        if attack_type == 'Psychic':
            attack_base -= .5
        if attack_type == 'Bug':
            attack_base += 1
        if attack_type == 'Ghost':
            attack_base += 1
        if attack_type == 'Dark':
            attack_base += 1
    if 'Bug' in attack_type_1:
        if attack_type == 'Fire':
            attack_base += 1
        if attack_type == 'Grass':
            attack_base -= .5
        if attack_type == 'Fighting':
            attack_base -= .5
        if attack_type == 'Ground':
            attack_base -= .5
        if attack_type == 'Flying':
            attack_base += 1
        if attack_type == 'Rock':
            attack_base += 1
    if 'Rock' in attack_type_1:
        if attack_type == 'Normal':
            attack_base -= .5
        if attack_type == 'Fire':
            attack_base -= .5
        if attack_type == 'Water':
            attack_base += 1
        if attack_type == 'Grass':
            attack_base += 1
        if attack_type == 'Fighting':
            attack_base += 1
        if attack_type == 'Poison':
            attack_base -= .5
        if attack_type == 'Ground':
            attack_base += 1
        if attack_type == 'Flying':
            attack_base -= .5
        if attack_type == 'Steel':
            attack_base += 1
    if 'Ghost' in attack_type_1:
        if attack_type == 'Normal':
            attack_base = 0
        if attack_type == 'Fighting':
            attack_base = 0
        if attack_type == 'Poison':
            attack_base -= .5
        if attack_type == 'Bug':
            attack_base -= .5
        if attack_type == 'Ghost':
            attack_base += 1
        if attack_type == 'Dark':
            attack_base += 1
    if 'Dragon' in attack_type_1:
        if attack_type == 'Fire':
            attack_base -= .5
        if attack_type == 'Water':
            attack_base -= .5
        if attack_type == 'Electric':
            attack_base -= .5
        if attack_type == 'Grass':
            attack_base -= .5
        if attack_type == 'Ice':
            attack_base += 1
        if attack_type == 'Dragon':
            attack_base += 1
        if attack_type == 'Fairy':
            attack_base += 1
    if 'Dark' in attack_type_1:
        if attack_type == 'Fighting':
            attack_base += 1
        if attack_type == 'Psychic':
            attack_base = 0
        if attack_type == 'Bug':
            attack_base += 1
        if attack_type == 'Ghost':
            attack_base -= .5
        if attack_type == 'Dark':
            attack_base -= .5
        if attack_type == 'Fairy':
            attack_base += 1
    if 'Steel' in attack_type_1:
        if attack_type == 'Normal':
            attack_base -= .5
        if attack_type == 'Fire':
            attack_base += 1
        if attack_type == 'Grass':
            attack_base -= .5
        if attack_type == 'Ice':
            attack_base -= .5
        if attack_type == 'Fighting':
            attack_base += 1
        if attack_type == 'Poison':
            attack_base = 0
        if attack_type == 'Ground':
            attack_base += 1
        if attack_type == 'Flying':
            attack_base -= .5
        if attack_type == 'Psychic':
            attack_base -= .5
        if attack_type == 'Bug':
            attack_base -= .5
        if attack_type == 'Rock':
            attack_base -= .5
        if attack_type == 'Dragon':
            attack_base = 1
        if attack_type == 'Steel':
            attack_base -= .5
        if attack_type == 'Fairy':
            attack_base -= .5
    if 'Fairy' in attack_type_1:
        if attack_type == 'Fighting':
            attack_base -= .5
        if attack_type == 'Poison':
            attack_base += 1
        if attack_type == 'Bug':
            attack_base -= .5
        if attack_type == 'Dragon':
            attack_base = 0
        if attack_type == 'Dark':
            attack_base -= .5
        if attack_type == 'Steel':
            attack_base += 1

    return attack_base
