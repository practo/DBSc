from __future__ import print_function
from sqlalchemy import create_engine
from sqlalchemy.engine import reflection
import sys
from dbsc.settings import CONNECTION_STRING

engine = create_engine(CONNECTION_STRING)
insp = reflection.Inspector.from_engine(engine)

if __name__ == "__main__":
    for table_name in insp.get_table_names():
        print('[' + table_name + '] {color:blue}')
        primary_keys = insp.get_primary_keys(table_name)
        foreign_keys = insp.get_foreign_keys(table_name)
        for column in insp.get_columns(table_name):
            print(' ', end='')
            if column['name'] in primary_keys:
                print('*', end='')
            else:
                print(' ', end='')
            print(column['name'], end='')
            if any(column['name'] in fk['constrained_columns']
                   for fk in foreign_keys):
                print('*')
            else:
                print('')
        print('')

    for table_name in insp.get_table_names():
        for foreign_key in insp.get_foreign_keys(table_name):
            print('[' + foreign_key['referred_table'] + '] 1--* [' + table_name +
                  ']')
