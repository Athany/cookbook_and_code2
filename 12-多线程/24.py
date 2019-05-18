import multiprocessing
from time import ctime


def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q")
    print("Out of consumer:", ctime())

def producer(sequence, output_q):
    for item in sequence:
        print("Into procuder:", ctime())
        output_q.put(item)
        print("Out of procuder:", ctime())


if __name__ == '__main__':
    q = multiprocessing.Queue()
    cons_p1 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p1.start()

    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p2.start()

    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    q.put(None)   # 哨兵，消费者取出None后就会退出，有几个消费者，放几个哨兵即可，不会冲突
    q.put(None)

    cons_p1.join()
    cons_p2.join()
