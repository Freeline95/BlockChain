from flask import Flask, jsonify
from blockchain import BlockChain

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

blockchain = BlockChain()


@app.route('/mine_block', methods=['GET'])
def mine_block():
    last_block = blockchain.get_last_block()
    new_proof = blockchain.proof_of_work(last_block.proof)

    mined_block = blockchain.create_block(new_proof, last_block.get_block_hash(), last_block)

    return jsonify(mined_block.serialize()), 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.serialize(),
                'length': len(blockchain.chain)}

    return jsonify(response), 200


@app.route('/is_valid', methods=['GET'])
def is_valid():
    response = {'valid': blockchain.validate()}

    return jsonify(response), 200


app.run(host='127.0.0.1', port=5000, debug=True)
