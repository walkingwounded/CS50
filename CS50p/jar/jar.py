####Week8-2 nomnomnom 🍪🍪🍪


###changing class self.# to self._#, important to change all self.# to self._# when returning values to class.
class Jar:
    def __init__(self, capacity=12):
        if capacity <0:
            raise ValueError("Invalid Input")
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        return ("🍪"*self.size)

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many 🍪!!")
        else:
            self._size += n
            return self._size

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough 🍪!!")
        else:
            self._size -= n
            return self._size

###change return self._capacity as self.capacity has been used
    @property
    def capacity(self):
        return self._capacity

###change return self._size as self.size has been used
    @property
    def size(self):
        return self._size


####print test
# jar = Jar()
# jar.deposit(5)
# jar.withdraw(4)
# print(jar)