from uclcoin import Block, KeyPair
import requests
import json
from collections import namedtuple

wallet = KeyPair("10c3e7593eb0525c10652c835e85f8e709e897bf891ef9fd9451c94755690ccf")
r = requests.get('https://uclcriptocoin2.herokuapp.com/block/minable/' + wallet.public_key)
print(r.text)
last_block = json.loads(r.text)
block = Block.from_dict(last_block["block"])
difficulty = last_block["difficulty"]

while block.current_hash[:difficulty].count('0') < difficulty:
    block.nonce += 1
    block.recalculate_hash()

data = json.dumps(block, default=lambda x: x.__dict__)

response = requests.post('https://uclcriptocoin2.herokuapp.com/block',data,json=True)
print(response.text)
