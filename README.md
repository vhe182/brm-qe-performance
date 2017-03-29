# brm-qe-performance

Scripts for running performance tests against the Billing and Revenue
Management system.

## Description

Scripts are separated into scenarios.

|Performance Test   |Description    |Run Location   |
|-------------------|-------------------|-------------------|
|rate-load.py           |Rating and Loading of Daily and Monthly account data |brmpipe2|
|bill-pay.py            |Bill Payment for US and UK accounts |brmapp1|
|payment-collect.py     |Collect payments and send to PSL |brmapp1|
|get-payment-batch.py   |Batch payments and send to |brmapp1|
