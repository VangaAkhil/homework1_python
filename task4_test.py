from task4 import discount


def test_discount():
  final_price = discount(200, 10)
  assert final_price == 180.0


def test_discount_with_diff_values():
  final_price = discount(129.5, 15)
  assert final_price == 127.925


def test_discount_with_invalid_values():
  try:
    discount("20", 10)
  except ValueError as e:
    assert str(e) == "price and discount must be numeric."
