init:
	pip install -r requirements.txt

test:
	py.test --cov=create_parking_lot --cov=console_app tests/

