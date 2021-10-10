                                                                                                                                                                                                                                                                                                                                                                                                                                   import json
data = {
"title": "Astrophysics for People in a Hurry",
"pages": "144",
"year": "2017",
"author": "Neil DeGrasse Tyson"
}

with open('books.json', 'w') as file:
    json.dump(data, file)

