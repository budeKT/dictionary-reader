import requests

def get_definition(word):
    """
    returns all the details of the given word
    """
    Base_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    # sends a request to the dictionary API and stores the dictionary
    json_text = requests.get(Base_URL + word)
    # if the word is not found
    if json_text.status_code == 404:
        print("Word not found")
    else:
        #convert the Json format to python dictionaries
        data = json_text.json()
        meanings = data[0]["meanings"]
        # lists all the definitions
        for item in meanings:
            print(item["partOfSpeech"].capitalize()+ ":")
            for number, definitions in enumerate(item["definitions"]):

                if number and len(definitions) == 4:
                    # different partOfSpeech may not have any examples.
                    print(f"{number+1}. {definitions['definition']}")
                    print(f"Example: {definitions['example']}")
                    print("\n")
                elif number > 4:
                    # Some words may have many defs which will get redundant
                    break
                else:
                    print(f"{number+1}. {definitions['definition']}")
                    print("\n")
        
def main():
    word = input("Enter a Word: ")
    get_definition(word)
    
if __name__ == '__main__':
    main()