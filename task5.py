favorite_books = [{
    "title": "half girlfriend",
    "author": "munna bhai"
}, {
    "title": "titanic",
    "author": "smatil"
}, {
    "title": "baby",
    "author": "chiru"
}]

books = favorite_books[0:3]
print("First three fav books are:")
for book in books:
  print(f" title : {book['title']} : author : {book['author']}")

student_database = {
    "student1": {
        "name": "munna",
        "age": 22
    },
    "student2": {
        "name": "chinna",
        "age": 18
    },
    "student3": {
        "name": "kanna",
        "age": 26
    },
}

studentName = student_database["student1"]["name"]
studentAge = student_database["student1"]["age"]

print(f"Student info:\nName: {studentName}\nAge: {studentAge}")
