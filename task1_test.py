import task1

def testing_hello_replit(capsys):

  task1.print_hello()
  actual = capsys.readouterr().out
  expected = "Hello Replit!\n"
  assert actual == expected
