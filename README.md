## rw-data-coding-test

Running the shell command will execute the script in the aggregate.py file that:
1. loads the csv data into the database
1. formats the auction_timestamp column to allow the use of sqlite datetime functions
1. selects the desired aggregations
1. prints the desired aggregations to the console

## To run
```bash
python aggregate.py
```