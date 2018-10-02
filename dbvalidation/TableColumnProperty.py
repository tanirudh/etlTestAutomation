class TableColumProperty:
  column_name=None
  column_type=None
  column_size=None
  column_isnull=None

  def __init__(self, cname, ctype, csize, cisnull):
    self.column_name=cname
    self.column_type=ctype
    self.column_size=csize
    self.column_isnull=cisnull
