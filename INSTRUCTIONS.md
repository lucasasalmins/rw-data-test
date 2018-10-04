# rw-data-coding-test

## Task

The task is essentially to take the supplied CSV file (`./dataset.csv`) and manipulate it to produce a dataset that can be used to perform specific aggregations against the data.

The file contains > 1000 records of auction results for the 3 eastern Australian states (NSW, VIC, QLD) over a recent 7 week period. 

The aggregates that need to be produced are:
- mean sale price for each state, for each week.
- mean sale price for each capital city area, for each week.

The only hard technological requirements of the task are the *SQLite3* be used as the datastore, and that the aggregates are produced as queries against some table in an SQLite database.

While it's not a hard requirement, we _recommend_ using python for loading of the database, and parsing of the data.

### About the file

- `sale_price` and `outcome`  are (ostensibly) self reported by the estate agents, while their type is enforced in the reporting system, there is no guarantee that the agent *has* reported, or reported completely - so many values might be missing.
- Fields pertaining to the address have been automatically populated, but by several different services. There is no guarantee that a reference to the same entity (such as a state) are consistent between records.
- `capital_city` refers to the greater capital city area (according to the ABS) that a listing falls into (if any).
- `auction_id` *should* be globally unique, it's our internal identifier for an auction.
- `auction_timestamp` refers to the UTC time at which the auction was scheduled to take place.

## Submission

The submission should come in the form as the same repository, with additional commits and instructions for running your code. Ideally, we'll be able to execute a single shell command and have the database built from the CSV file and the aggregate result reporting to the shell. 

We don't expect you to spend more than 2 hours on the task, and it's perfectly OK if you do not complete it. Our intention is to verify that you can write code (at whatever your level is), gauge your ability to approach a rather ambiguous project, and to produce talking points for interrogation in a subsequent interview. 

If you have any questions, please don't hesitate to get in touch with us:

Matt: mgay@raywhite.com
Adrian: agimenez@raywhite.com
