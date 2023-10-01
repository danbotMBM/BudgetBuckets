# Bucket Budgeting app

## File Description
|File| Use|
|---|---|
|budget.py| contain the object logic for budgeting using buckets|
|digest.py| process a new set of transactions and cross reference with old transactions to replace transactions that were pending|
|settings.py| global set of adjustable variables|
|label.py| take in transactions and quicky label them with the user|

### Timeframes
Timeframes are however long a bucket lasts before they are recycled (all excess money is removed and redistributed).

| Timeframe title | Start date |
| ---    | ---     |
| yearly | first of the month created |
| montly | first of the month created |
| weekly | most recent monday in the past/present of week created|



 