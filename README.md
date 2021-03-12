Install python3.7 or higher

Install Flask(micro-framework) via:
pip install Flask==0.12.2 --user
If you have an error, that pip command is undefined, then run next command:
pip3 install Flask==0.12.2 --user

Run python3 app.py to start the server (it is daemon script)
Now it is running on localhost:5000

Application has 2 routes:
1) localhost:5000/mine_block - create new block in blockchain
2) localhost:5000/get_chain - dump all blocks in chain