#creating a mad libs game - ask for words and add them to the correct places - use append???
'''
Strings
Variables
Concatenation
Print
'''
if __name__ == '__main__':
    adjective1 = input("Tell me an adjective ")
    adjective2 = input("Tell me an another adjective ")
    adjective3 = input("Tell me an another adjective ")
    adjective4 = input("Tell me an another adjective ")
    adjective5 = input("Tell me an another adjective ")
    adjective6 = input("Tell me an another adjective ")
    noun1 = input("Tell me a noun ")
    noun2 = input("Tell me a another noun ")
    plural_noun1 = input("Tell me a plural noun ") 
    plural_noun2 = input("Tell me a another plural noun ") 
    plural_noun3 = input("Tell me a another plural noun ") 
    plural_noun4 = input("Tell me a another plural noun ") 
    person_in_room_female = input("Tell me a name of a female ") 
    article_of_clothing = input("Tell me an article of clothing ") 
    a_place = input("Tell me a place ") 
    a_city = input("Tell me a city ") 
    part_of_the_body = input("Tell me a part of the body ") 
    letter_of_the_alphabet = input("Tell me a letter of the alphabet ") 
    verb = input("Tell me a verb ") 
    number = input("Tell me a number ") 
    celebrity = input("Tell me a celebrity ") 
    mad_lib_template = f'''There are many {adjective1} ways to choose a/an {noun1} to read. 
    First, you could ask for recommendations from your friends and {plural_noun1}. 
    Just don’t ask Aunt {person_in_room_female} - she only reads {adjective2} books with {article_of_clothing}-ripping goddesses on the cover. 
    If your friends and family are no help, try checking out the {noun2} Review in The {a_city} Times. 
    If the {plural_noun2} featured there are too {adjective3} for your taste, try something a little more low-{part_of_the_body}, like {letter_of_the_alphabet}: The {celebrity} Magazine, or {plural_noun3} Magazine. 
    You could also choose a book the {adjective4}-fashioned way Head to your local library or {a_place} and browse the shelves until something catches your {part_of_the_body}. 
    Or you could save yourself a whole lot of {adjective5} trouble and log on to www.bookish.com, the {adjective6} new website to {verb} for books! With all the time you’ll save not having to search for {plural_noun4}, you can read {number} more books!
    '''
    print(mad_lib_template)