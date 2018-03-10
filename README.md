# bc_bc_bc
A sample blockchain implementation.

This code works with Python3.
You need to install Flask, cURL.
To install Flask:
	sudo pip3 install flask
To install cURL:
	brew install curl

To run this code:
Open two terminals.
1st terminal:
  python3 bc_startPOS.py
 
2nd terminal:
  This terminal will be used to make server call to mine, display blocks, create transactions.
  
  To create transactions:
  curl "localhost:5000/comeOver" \
     -H "Content-Type: application/json" \
     -d '{"from": "ramharivitthala", "to":"shamharivitthala", "amount": 29}'
  
  To display blocks:
  curl localhost:5000/blocks
  
  To mine:
  curl localhost:5000/mine
