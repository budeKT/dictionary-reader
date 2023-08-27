import requests

def get_definition(word):
    """
    returns all the details of the given word
    """
    Base_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    # sends a request to the dictionary API and stores the dictionary
    json_text = requests.get(Base_URL + word)
    # if the word is not found
    # Max amount of definitions to retrieve
    if json_text.status_code == 404:
        print("Word not found")
    else:
        #convert the Json format to python dictionaries
        data = json_text.json()
        meanings = data[0]["meanings"]
        partOfSpeech = []
        definition = []
        example = []
        # lists all the definitions
        for item in meanings:
            # print(item["partOfSpeech"].capitalize()+ ":")
            for number, definitions in enumerate(item["definitions"]):
                if (len(definitions) == 4):
                    # different partOfSpeech may not have any examples.
                    # print(f"{number+1}. {definitions['definition']}")
                    # print(f"Example: {definitions['example']}")          
                    partOfSpeech.append(item["partOfSpeech"])
                    definition.append(definitions['definition'])
                    example.append(definitions['example'])
                else:
                    # print(f"{number+1}. {definitions['definition']}")
                    partOfSpeech.append(item["partOfSpeech"])
                    definition.append(definitions['definition'])
                    example.append("Not Available.")\
                    
            maxIndex = len(definition)
        
        return partOfSpeech, definition, example, maxIndex
def main(word):
    definedWord = get_definition(word)

    if definedWord == None:
        return "Word not found. Please try again."
    else:
        return definedWord
    
if __name__ == '__main__':
    main()