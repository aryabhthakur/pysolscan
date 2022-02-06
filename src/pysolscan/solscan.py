from requests import request
    
def buildurl(param:dict=None,path=str): # Common function to assemble request url components(Parameters, Path & Header) and make call.
        header = {
            'accept': 'application/json',
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
            }
        req = request('GET','https://public-api.solscan.io'+path,params=param,headers=header)
        return req.json()
    
    # Related-to : https://public-api.solscan.io/block/last?limit=10
def get_last_block(limit:int=10):
        if isinstance(limit,int) == True:
            result = buildurl(param={"limit":limit},path='/block/last')
            return result
        else:
            return 'Limit is not Integer'

    # Related-to : https://public-api.solscan.io/block/transactions?block={{blockID}}&offset=0&limit=10
def get_block_transactions(limit:int=10,offset:int=0,block=None):
        if block is not None:
            if isinstance(limit,int) == True & isinstance(offset,int) == True: 
                result =  buildurl(param={"limit":limit,"offset":offset,"block":block},path='/block/transactions')
                return result
            else:
                return 'Limit or Offset is not Integer'
        else:
            return 'Block not Specified'
    
    # Related-to : https://public-api.solscan.io/block/{{blockID}}
def get_block_info(block:int=None):
        if isinstance(block,int) == True:
            result =  buildurl(path='/block/%s'%block)
            return result
        else:
            return 'Block is not Integer'
    
    # Related-to : https://public-api.solscan.io/transaction/last?limit=10
def get_last_transaction(limit:int=10):
        if isinstance(limit,int) == True:
            result = buildurl(param={"limit":limit},path='/transaction/last')
            return result
        else:
            return 'Limit is not Integer'
    
    # Related-to : https://public-api.solscan.io/transaction/{{transactionSignature}}
def get_transaction_signature_info(signature:str=None):
        if signature is not None:
            result = buildurl(path='/transaction/%s'%signature)
            return result
        else:
            return 'Signature not Specified'
    
    # Related-to : https://public-api.solscan.io/account/tokens?account={{accountID}}
def get_account_token(account:str=None):
        if account is not None:
            result = buildurl(param={"account":account},path='/account/tokens')
            return result
        else:
            return 'Account not Specified'
    
    # Related-to : https://public-api.solscan.io/account/transactions?account={{accountID}}&beforeHash={{beforeHash}}&limit=10
def get_account_transaction(account:str=None,beforeHash:str=None,limit:int=10):
        if account is not None:
            param = {"account":account,"beforeHash":beforeHash,"limit":limit}
            if param['beforeHash'] == None:
                del param['beforeHash']
            if isinstance(limit,int) == True:
                    result = buildurl(param=param,path='/account/transactions')
                    return result
            else:
                    return 'Limit is not Integer'
        else:
            return 'Account not Specified'
    
    # Related-to : https://public-api.solscan.io/account/stakeAccounts?account={{accountID}}
def get_account_stakeAccounts(account:str=None):
        if account is not None:
            result = buildurl(param={"account":account},path='/account/stakeAccounts')
            return result
        else:
            return 'Account not Specified'
    
    # Related-to : https://public-api.solscan.io/account/splTransfers?account={{accountID}}&offset=0&limit=10
def get_account_splTransfers(account:str=None,limit:int=10,offset:int=0,fromTime:int=None,toTime:int=None):
        if account is not None:
            param = {"account":account,"fromTime":fromTime,"toTime":toTime,"limit":limit,"offset":offset}
            if param['toTime'] == None:
                del param['toTime'] 
            if param['fromTime'] == None:
                del param['fromTime'] 
            result = buildurl(param=param,path='/account/splTransfers')
            return result
        else:
            return 'Account not Specified'
    
    # Related-to : https://public-api.solscan.io/account/solTransfers?account={{accountID}}&offset=0&limit=10
def get_account_solTransfers(account:str=None,limit:int=10,offset:int=0,fromTime:int=None,toTime:int=None):
        if account is not None:
            param = {"account":account,"fromTime":fromTime,"toTime":toTime,"limit":limit,"offset":offset}
            if param['toTime'] == None:
                del param['toTime'] 
            if param['fromTime'] == None:
                del param['fromTime'] 
            result = buildurl(param=param,path='/account/solTransfers')
            return result
        else:
            return 'Account not Specified'
    
    # Related-to : https://public-api.solscan.io/account/exportTransactions?account={{accountID}}&type={{tokenchange|solTransfers|all}}&fromTime={{timestamp}}&toTime={{timestamp}}
def get_account_exportTransactions(account:str=None,type:str='all',fromTime:int=None,toTime:int=None):
        if account is not None:
            param = {"account":account,"fromTime":fromTime,"toTime":toTime,"type":type}
            if param['toTime'] == None:
                del param['toTime'] 
            if param['fromTime'] == None:
                del param['fromTime'] 
            result = buildurl(param=param,path='/account/exportTransactions')
            return result
        else:
            return 'Account & FromTime (Timestamp) & ToTime (Timestamp) & Type is required'
    
    # Related-to : https://public-api.solscan.io/account/{{accountID}}
def get_account_info(account:str=None):
        if account is not None:
            result = buildurl(path='/account/%s'%account)
            return result.json()
        else:
            return 'Account & FromTime (Timestamp) & ToTime (Timestamp) & Type is required'
    
    # Related-to : https://public-api.solscan.io/token/holders?tokenAddress={{tokenaddr}}&offset=0&limit=10
def get_token_holder(tokenaddr:str=None,limit=10,offset=0):
        if tokenaddr is not None:
            result =  buildurl(param={"tokenAddress":tokenaddr,"offset":offset,"limit":limit},path='/token/holders')
            return result
        else:
            return 'Token address Required'
        
    # Related-to : https://public-api.solscan.io/token/meta?tokenAddress={{tokenaddr}}
def get_token_meta(tokenaddr:str=None):
        if tokenaddr is not None:
            result = buildurl(param={"tokenAddress":tokenaddr},path='/token/meta/')
            return result
        else:
            return 'Token Address required'

    # Related-to : https://public-api.solscan.io/token/list?sortBy={{market_cap | volume | holder | price | price_change_24h | price_change_7d | price_change_14d | price_change_30d | price_change_60d | price_change_200d | price_change_1y}}&direction=desc&limit=10&offset=0
def get_token_list(sortBy:str='market_cap',direction:str='desc',limit=10,offset=0):
        result =  buildurl(param={"sortBy":sortBy,"direction":direction,"limit":limit,"offset":offset},path='/token/list')
        return result

    # Related-to : https://public-api.solscan.io/market/token/{{tokenaddr}}
def get_market_token_info(tokenaddr:str=None):
    if tokenaddr is not None:
        result = buildurl(path='/market/token/%s'%tokenaddr)
        return result
    else:
        return 'Token Address required'

    # Related-to : https://public-api.solscan.io/chaininfo/
def get_chaininfo():
        result = buildurl(path='/chaininfo')
        return result