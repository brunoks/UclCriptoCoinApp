from uclcoin import Block, KeyPair, BlockChain
import requests
import json
from collections import namedtuple


r = requests.get('https://uclcriptocoin.herokuapp.com/block/minable/03ecd19ebc9454eb635670577c24ad34a61fa05c23ce47f142fe704f6b37f59708')
last_block = json.loads(r.text)
block = Block.from_dict(last_block["block"])
difficulty = last_block["difficulty"]

while block.current_hash[:difficulty].count('0') < difficulty:
    block.nonce += 1
    block.recalculate_hash()

data = json.dumps(block, default=lambda x: x.__dict__)

requests.post('https://uclcriptocoin.herokuapp.com/block',data,json=True)
print(requests)




































