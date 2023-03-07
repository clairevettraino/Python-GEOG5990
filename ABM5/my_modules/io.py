import csv

def read_data():
    f = open('C:/Users/cgkve/Desktop/Python/data/input/in.txt', newline='')
    data = [] 
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
            print(value)
        data.append(row)
        n_rows = max(row)
        n_cols = max(line)
    f.close()
    return  
    print(data)
