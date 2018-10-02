import json
import sys
from difflib import get_close_matches

def main():
    dict_data = open("data.json", "r", encoding="utf8")
    json_data = json.load(dict_data)

    user_input = input("Define: ")

    if user_input in json_data:
        for data in json_data[user_input]:
            print("{}: {}".format(user_input, data))
    else:
        closest_word = get_close_matches(user_input, json_data.keys(), 1)
        for word in closest_word:
            res = input(user_input + " " +"was not found, did you mean " + word + " if yes type Y and if no type N: ")
            print(res)
            if res == "y":
                print(str(json_data[word]))
            elif res == "n":
                print("the program is ending")
                sys.exit()
        if user_input not in json_data:
            print("did not find the word")

if __name__ == '__main__':
    main()
