class company():
    def __init__(self):
        self.__companyName="Google" #__ = access specifier:which can only access within the method

    def companyName(self):
        print(self.__companyName)

c1=company()
c1.companyName()
print(c1.__companyName)

class company():
    def __init__(self):
        self._companyName="Google" #_ = access specifier(protected)

c1=company()
print(c1._companyName)
