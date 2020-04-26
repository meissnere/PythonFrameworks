# import package for JSON modules
import json

# open function in read only, with means file is closed
# when the code block exits
with open('input.json', 'r') as input:
    obj = json.load(input)
    with open('output.txt', 'w') as output:
        output.write(obj['name'] + "'s Hobbies are:\n")
        for hobby in obj['hobbies']:
            output.write(hobby + "\n")