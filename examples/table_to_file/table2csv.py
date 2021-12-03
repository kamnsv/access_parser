#pip install pandas
#pip install access-parser

from access_parser import AccessParser
import pandas as pd
from tabulate import tabulate
import argparse

class SaveParse(AccessParser):
    def save_table(self, table_name, out): 
        table = self.parse_table(table_name)
        df = pd.DataFrame()
        for i in table:
            df[i] = list(table[i])
        df.to_csv(table_name+'.csv', index=False) 
    
def save_table(args):
    db = SaveParse(args.file)
    db.save_table(args.table, args.out)
    
def print_tables(db_path, only_catalog=False, specific_table=None):
    db = AccessParser(db_path)
    if only_catalog:
        for k in db.catalog.keys():
            print(f"{k}\n")
    elif specific_table:
        table = db.parse_table(specific_table)
        print(f'TABLE NAME: {specific_table}\r\n')
        print(tabulate(table, headers="keys"))
        print("\n\n\n\n")
    else:
        db.print_database()

def start_parse(args):
    if args.out:
        return save_table(args)
    print_tables(args.file, args.catalog, args.table)
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--catalog",  required=False, help="Print DB table names", action="store_true")
    parser.add_argument("-f", "--file",     required=True,  help="*.mdb / *.accdb File")
    parser.add_argument("-t", "--table",    required=False, help="Table to print", default=None)
    parser.add_argument("-o", "--out",      required=False, help="Out file save for the table",  action="store_true")
    
    args = parser.parse_args()
    start_parse(args)
    
