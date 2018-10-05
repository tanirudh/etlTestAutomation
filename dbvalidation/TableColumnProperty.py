class TableColumnProperty(object):

    def __init__(cls, cname, ctype):
        cls.column_name=cname
        cls.column_type=ctype

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__
    
    def __hash__(self):
        return hash((self.column_name, self.column_type))