import threading

balance = 0

def withdraw(amount):
    global balance
    balance -= amount

def deposit(amount):
    global balance
    balance += amount

if __name__ == '__main__':
    t1 = threading.Thread(target=withdraw, args=(100,))
    t2 = threading.Thread(target=deposit, args=(100,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(balance)
