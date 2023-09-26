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


#Test Cases
def test1():
  assert isinstance(favorite_books, list)
  assert favorite_books[0]['title'] == "half girlfriend"
  assert favorite_books[1]['author'] == "chintu"
  assert favorite_books[2]['title'] == "baby"


def test2():
  assert isinstance(student_database, dict)
  assert student_database['student1']['name'] == "munna"
  assert student_database['student3']['age'] == 26

test1()
test2()

