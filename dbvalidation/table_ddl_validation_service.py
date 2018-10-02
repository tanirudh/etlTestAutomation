import csv
from TableColumnProperty import TableColumnProperty
def load_csv_data(filename):
    column_properties = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, ['name', 'type', 'size', 'isnull'])
        for row in reader:
            print('------------:' + row['name'] + ',' + row['type'] + ',' + row['size'] + ',' + row['isnull'])
            tmp =  TableColumnProperty(row['name'], row['type'], row['size'], row['isnull'])
            print(tmp)
            # column_properties.append(TableColumnProperty(row['name'], row['type'], row['size'], row['isnull']))
    return column_properties
