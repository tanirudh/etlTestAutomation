import csv
import TableColumnProperty

def load_csv_data(filename):
    column_properties = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, ['name', 'type'])
        for row in reader:
            column_properties.append(TableColumnProperty.TableColumnProperty(row['name'].strip(' \t\n\r'), row['type'].strip(' \t\n\r')))
    return column_properties
