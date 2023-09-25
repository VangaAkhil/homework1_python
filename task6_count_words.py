def count_words(filename):
  try:
    with open(filename, 'r') as file:
      content = file.read()
      words = content.split()
      count = len(words)
      return count
  except FileNotFoundError:
    print(f"The file '{filename}' not found.")
    return None


filename = "content.txt"
count = count_words(filename)
count1 = count_words("content1.txt")

if count is not None:
  print(f"Total words : '{filename}': {count}")


#Test Cases
def testing_words_count():
  assert count_words("content.txt") == count
  assert count_words("content1.txt") == count1
