import sqlite3
import csv

# create or connect to db
db = sqlite3.connect('ray_whitedb')

# create a cursor object
cursor = db.cursor()

# drop table if exists
cursor.execute("DROP TABLE IF EXISTS dataset;")

# create table
cursor.execute(
    '''
      CREATE TABLE IF NOT EXISTS dataset
      (
        auction_id        TEXT,
        listing_id        INTEGER,
        listing_date      TEXT,
        auction_timestamp TEXT,
        street_address    TEXT,
        suburb            TEXT,
        postcode          INTEGER,
        capital_city      TEXT,
        state             TEXT,
        outcome           TEXT,
        sale_price        INTEGER
      );
    ''')

# read from csv
with open('dataset.csv', 'rt') as dataset:
  dr = csv.DictReader(dataset)
  to_db = [(
      i['auction_id'],
      i['listing_id'],
      i['listing_date'],
      i['auction_timestamp'],
      i['street_address'],
      i['suburb'],
      i['postcode'],
      i['capital_city'],
      i['state'],
      i['outcome'],
      i['sale_price'],
  ) for i in dr]

# insert data into table
cursor.executemany(
    '''
      INSERT INTO dataset
      (
        auction_id        ,
        listing_id        ,
        listing_date      ,
        auction_timestamp ,
        street_address    ,
        suburb            ,
        postcode          ,
        capital_city      ,
        state             ,
        outcome           ,
        sale_price
      )
      VALUES
      (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    ''', to_db)

# remove 'UTC' substring from datetime string to allow use of sqlite datetime functions
cursor.execute(
    '''
      UPDATE
      dataset
      SET auction_timestamp=REPLACE(auction_timestamp, ' UTC', '');
    '''
)

db.commit()

# get mean sale price for each state, for each week.
cursor.execute(
    '''
      SELECT
        AVG(sale_price),
        state,
        strftime('%W', auction_timestamp) week
      FROM dataset
      GROUP BY
        state,
        week
      ORDER BY
        week;
    '''
)

mean_by_state = cursor.fetchall()

# get mean sale price for each capital city area, for each week.
cursor.execute(
    '''
      SELECT
        AVG(sale_price),
        capital_city,
        strftime('%W', auction_timestamp) week
      FROM dataset
      GROUP BY
        capital_city,
        week
      ORDER BY
        week;
    '''
)
mean_by_capital = cursor.fetchall()
db.close()

dash = '-' * 40

# format and print to console
for i in range(len(mean_by_state)):
  if i == 0:
    print(dash)
    print('{:<16s}{:<17s}{:<12s}'.format('MEAN', 'STATE', 'WEEK'))
    print(dash)
  else:
    print('{:<16f}{:<17s}{:<12s}'.format(mean_by_state[i][0], mean_by_state[i][1], mean_by_state[i][2]))

for i in range(len(mean_by_capital)):
  if i == 0:
    print(dash)
    print('{:<16s}{:<17s}{:<12s}'.format('MEAN', 'CAPITAL', 'WEEK'))
    print(dash)
  else:
    print('{:<16f}{:<17s}{:<12s}'.format(mean_by_capital[i][0], mean_by_capital[i][1], mean_by_capital[i][2]))
