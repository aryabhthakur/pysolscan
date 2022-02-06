# PySolscan
_____
#### It's a minimal wrapper around Solscan.io API

##### Block -
- ```get_last_block(limit=10)```  Get last **[limit]** blocks (Default Limit: **10**)
- ```get_block_transactions(limit=10,offset=0,block=None)``` Get block transactions.
- ```get_block_info(block=None)```  Detail information of given block.

##### Transaction -
- ```get_last_transaction(limit=10)``` Get last [limit] transactions
- ```get_transaction_signature_info(signature=None)``` Detail information of given transaction signature 

##### Account -
- ```get_account_token(account=None)```  Get token balances of the given account
- ```get_account_transaction(account=None,beforeHash=None,limit=10)``` Get list of transactions of the given account.
- ```get_account_stakeAccounts(account=None)``` Get staking accounts of the given account
- ```get_account_splTransfers(account=None,limit=10,offset=0,fromTime=None,toTime=None)``` Get list of transactions make tokenBalance changes.
-  ```get_account_solTransfers(account=None,limit=10,offset=0,fromTime=None,toTime=None)``` Get list of SOL transfers
-  ```get_account_exportTransactions(account=None,type='all',fromTime=None,toTime=None)``` Export transactions to CSV. Returns **Blob** URL
-  ```get_account_info(account=None)``` Get overall account information, including program account, NFT metadata information

##### Token -
- ``` get_token_holder(tokenaddr=None,limit=10,offset=0)``` Get token holders
- ``` get_token_meta(tokenaddr=None)``` Get metadata of given token
- ``` get_token_list(sortBy='market_cap',direction='desc',limit=10,offset=0)``` Get list of tokens.

##### Market -
- ``` get_market_token_info(tokenaddr=None)``` Get market information of the given token

##### Chain Information -
- ``` get_chaininfo()``` Get market information of the given token


## Installation
PySolscan package is available via Pipy or Github.

```sh
pip install pysolscan
```

## Plugins

PySolscan doesn't require many packages except Python Requests

| Package | Pipy |
| ------ | ------ |
| Python Requests | https://pypi.org/project/requests/ |


## License
MIT

