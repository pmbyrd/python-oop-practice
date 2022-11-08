"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        "Create serial and set counter"
        self.start = start
        self.counter = start

    def __repr__(self):
        "Show represenstation"
        return f"<SerialGenerator start={self.start} self={self.counter}>"   
        
    def generate(self):
        "Intiate counter by in increments of 1, First number should equal intial start value"
        self.counter += 1
        return self.counter - 1




    def reset(self):
        "Reset the counter to zero"
        self.counter = self.start
        
        


    


