from uclcoin import Block, KeyPair
import requests
import json
from collections import namedtuple


class Minerador(object):

    def minerarBloco(self, address):
        wallet = KeyPair(address)
        r = requests.get('https://uclcriptocoin.herokuapp.com/block/minable/' + wallet.public_key)
        print(r.text)
        last_block = json.loads(r.text)
        block = Block.from_dict(last_block["block"])
        difficulty = last_block["difficulty"]

        while block.current_hash[:difficulty].count('0') < difficulty:
            block.nonce += 1
            block.recalculate_hash()

        data = json.dumps(block, default=lambda x: x.__dict__)

        r = requests.post('https://uclcriptocoin.herokuapp.com/block',data,json=True)
        print(r.text)
        self.pesquisarBlocoPendente()

    def pesquisarBlocoPendente(self):
        r = requests.get('https://uclcriptocoin.herokuapp.com/pending_transactions')

        data = r.json()
        if int(len(data['transactions']) > 0):
            self.minerarBloco('10c3e7593eb0525c10652c835e85f8e709e897bf891ef9fd9451c94755690ccf')
        else:
            return 'Não tem mais bloco'

minerador = Minerador()

minerador.pesquisarBlocoPendente()