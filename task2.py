#Task-2 Variables


#Integer
def check_integer(num):
  return num


#FLaot and Double
def check_double(num):
  return num


#String
def check_string(name):
  return name


#Boolean
def check_bool(b):
  return b


#List
def check_list(li):
  return li


#Set
def check_set(s):
  return s


#Test cases
def testing_integer():
  assert check_integer(10) == 10
  assert check_integer(2000) == 2000


def testing_double():
  assert check_double(10.0) == 10.0
  assert check_double(30.99) == 30.99


def testing_string():
  assert check_string("munna") == "munna"
  assert check_string("chinna") == "chinna"


def testing_boolean():
  assert check_bool(True) == True
  assert check_bool(False) == False


def testing_list():
  assert check_list([1, 2, 3, 4]) == [1, 2, 3, 4]


def testing_set():
  assert check_set({1, 2, 3, 4}) == {1, 2, 3, 4}


if __name__ == "__main__":
  testing_integer()
  testing_double()
  testing_string()
  testing_boolean()
  testing_list()
  testing_set()
