# -*- coding:utf-8 -*-

def simple_coroutine():
    print('coroutine started')
    x = yield
    print('coroutine received:', x)


if __name__ == '__main__':
    gen = simple_coroutine()
    print(gen)
    next(gen)
    gen.send(42)
