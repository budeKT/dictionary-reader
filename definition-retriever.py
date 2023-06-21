import requests
def get_definition(word):
    """
    returns a definition from a user input
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
        definitions = data[0]["meanings"]
        # lists all the definitions
        for word in definitions:
            #finsi

def main():
    word = input("Enter a Word: ")
    get_definition(word)
    
if __name__ == '__main__':
    main()