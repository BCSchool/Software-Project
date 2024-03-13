import json

def assign_letter_grade(pop_rating = 0):
    r = pop_rating

    if r > 90:
        return 'A'
    elif r > 80:
        return 'B'
    elif r > 70:
        return 'C'
    elif r > 60:
        return 'D'
    elif r > 50:
        return 'F'
    elif r > 40:
        return 'G'
    elif r > 30:
        return 'H'
    else:
        return 'Z'
    
def get_description(letter_rating):
    with open("/spotify/static/spotify/descriptions.json") as json_file:
        data = json.load(json_file)

    print(f"{letter_rating} description: ", data[letter_rating][0]["Track"])

def format_rating(generated_rating = 0):
    return get_description(assign_letter_grade(generated_rating))