# -*- coding:utf-8 -*-


def simple_coroutine(a):
    print('coroutine start, a: ', a)
    b = yield a
    print('receive b: ', b)
    c = yield a+b
    print('received c: ', c)


if __name__ == '__main__':
    gen = simple_coroutine(14)
    print(next(gen))
    print(gen.send(29))
    gen.send(99)
