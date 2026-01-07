
full_dot = '●'
empty_dot = '○'

def create_character(name,strength,intelligence,charisma):
    stat_list = [strength, intelligence, charisma]
    if not isinstance(name,str):
        return 'The character name should be a string'

    if name == '':
        return 'The character should have a name'
    
    if len(name)>10:
        return 'The character name is too long'

    if ' ' in name:
        return 'The character name should not contain spaces'
    
    if not all(type(stats) is int for stats in stat_list):
        return 'All stats should be integers'
    if not all(stats >= 1 for stats in stat_list):
        return 'All stats should be no less than 1'
    if not all(stats<=4 for stats in stat_list):
        return 'All stats should be no more than 4'
    if sum(stats for stats in stat_list) != 7:
        return 'The character should start with 7 points'
    
    return f'''{name}
STR {full_dot*strength+empty_dot*(10-strength)}
INT {full_dot*intelligence+empty_dot*(10-intelligence)}
CHA {full_dot*charisma+empty_dot*(10-charisma)}'''

ren = create_character('ren',4,2,1)
print(ren)
