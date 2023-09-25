#checking weatger number is positive/negative/zero
def classifyNumber(num):
  if num > 0:
    return "positive"
  elif num < 0:
    return "negative"
  else:
    return "zero"


#finding prime number
def isPrime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


#sum of numbers
def sumOfNumbers():
  sum = 0
  num = 1
  while num <= 100:
    sum += num
    num += 1
  return sum


#Test Cases for each function
def test_classify_number():
  assert classifyNumber(90) == "positive"
  assert classifyNumber(-9) == "negative"
  assert classifyNumber(0) == "zero"


def test_primes():
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  calculated_primes = [i for i in range(30) if isPrime(i)]
  assert primes == calculated_primes[:10]


def test_numbers():
  assert sumOfNumbers() == sum(range(1, 101))


if __name__ == "__main__":
  test_classify_number()
  test_primes()
  test_numbers()
