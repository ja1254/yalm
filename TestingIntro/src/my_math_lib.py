class SimpleMathLib:

    def add(self, *args):
        return sum(args)
    
    def multiply(self, *args):

        result = 1

        for num in args:
            result *= num

        return result
    
    