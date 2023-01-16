
import json
from web3 import Web3
import requests
import random
import time

RPC = "https://polygon-rpc.com"
web3 = Web3(Web3.HTTPProvider(RPC))

ABI = json.loads( 
    '''

    [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"AllreadyClaimedObject","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"signer","type":"address"},{"internalType":"bytes32","name":"digest","type":"bytes32"},{"components":[{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"},{"internalType":"uint8","name":"v","type":"uint8"}],"internalType":"struct PhiClaim.Coupon","name":"coupon","type":"tuple"}],"name":"ECDSAInvalidSignature","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"}],"name":"NotAdminCall","type":"error"},{"anonymous":false,"inputs":[],"name":"Hello","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenid","type":"uint256"}],"name":"LogClaimObject","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"verifierAddress","type":"address"}],"name":"SetAdminSigner","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"condition","type":"string"},{"indexed":false,"internalType":"uint256","name":"tokenid","type":"uint256"}],"name":"SetCoupon","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"contractAddress","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"checkClaimedStatus","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"contractAddress","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"condition","type":"string"},{"components":[{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"},{"internalType":"uint8","name":"v","type":"uint8"}],"internalType":"struct PhiClaim.Coupon","name":"coupon","type":"tuple"}],"name":"claimQuestObject","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAdminSigner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"condition","type":"string"}],"name":"getCouponType","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"admin","type":"address"},{"internalType":"address","name":"adminSigner","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"phiClaimedLists","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"verifierAdderss","type":"address"}],"name":"setAdminSigner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"condition","type":"string"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"setCouponType","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]

'''
 )
CONCTRACT = '0x754e78bC0f7B487D304552810A5254497084970C'

CONCTRACT2 = '0x3D8C06e65ebf06A9d40F313a35353be06BD46038'


phi_address = web3.toChecksumAddress(CONCTRACT)
phi_contract = web3.eth.contract(phi_address, abi=ABI)

def Check(user_address):

    #Активация аккаунта
    r = requests.post('https://utils-api.phi.blue/v1/philand/action',json =  {"address":user_address,"type":"LOGIN"},)
    time.sleep(3)

    #Замена кнопки Check eligible
    r = requests.post('https://utils-api.phi.blue/v1/philand/campaign/check?address='+user_address,
                json={} )
    time.sleep(8)


    #Проверка на выполененые задания
    r = requests.get('https://utils-api.phi.blue/v1/philand/condition/check?address='+ user_address) 
    toClaimId = r.json()['result']


    r = requests.get('https://utils-api.phi.blue/v1/philand/leader/exp?address='+ user_address) 
    expa = r.json()['expGain']
    print(f'\n XP на акке = {expa} XP')


    #Не выполеннные задания
    r = requests.get('https://utils-api.phi.blue/v1/philand/condition/progress?address='+ user_address) 
    AllTask = r.json()['result']

    avaibleTask = []
    for i in toClaimId:
        avaibleTask.append([[a['Condition'],a['Value'],a['TokenId']] for a in AllTask if a['TokenId']==int(i)])
    avaibleTask = list(filter(None, avaibleTask))

    print('Доступны задания = ')
    for i in avaibleTask:
        print(i[0][0])

    return avaibleTask

def ForTX(user_address,avaibleTask):
    r = requests.get('https://object-api.phi.blue/v1/quest_objects?address=' + user_address + '&condition='+ avaibleTask[0] + '&value='+ str(avaibleTask[1])) 
    forTX = r.json()

    return forTX

def mint(privatekey,user_address):


    avaibleTasks = Check(user_address)
    for task in avaibleTasks:
        try:
            task = task[0]
            forTX = ForTX(user_address,task)
            tx = {
                    
                'type': '0x2',
                'nonce': web3.eth.getTransactionCount(user_address),
                'from': web3.toChecksumAddress(user_address),
                'chainId': web3.eth.chain_id,
            }
            tx['maxFeePerGas'] = (
            web3.toWei( (web3.eth.estimate_gas(tx) * 2)/999, 'gwei'))
            tx['maxPriorityFeePerGas'] =  web3.toWei( (web3.eth.estimate_gas(tx) * 1)/999, 'gwei')
            tx['gas'] = int(random.randint(115000, 150000))

            transaction = phi_contract.functions.claimQuestObject(
            web3.toChecksumAddress(CONCTRACT2),
            task[2],
            task[0]+str(task[1]),
            [forTX['coupon']['r'],forTX['coupon']['s'],forTX['coupon']['v']]
            ).buildTransaction(tx)

            signed_txn = web3.eth.account.sign_transaction(transaction, privatekey)

            txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

            txn_hash = (txn_hash).hex()

            print(f'\n{task[0] + str(task[1])} Заминчина')
            print(f'\n== Hash : {txn_hash} ')

            time.sleep(random.randint(10, 20))
        
        except Exception as e:
            print(e)



with open("private_keys.txt", "r") as f:
    keys_list = [row.strip() for row in f]


for privatekey in keys_list:
    address = web3.eth.account.from_key(privatekey).address
    balance = Web3.fromWei(web3.eth.get_balance(web3.toChecksumAddress(address)), 'ether') 
    print(f'\n== Адрес : {address} //// Баланс = {balance} $MATIC ')

    mint(privatekey,address)

    #Промежуток между след. кошельком 1-5 секунд
    time.sleep(random.randint(1, 5))
