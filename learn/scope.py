test = dict(name='arm', age=35)


def test_scope():
  def test_scope_2():
    print(test)
  test_scope_2()



if __name__ == '__main__':
  test_scope()
