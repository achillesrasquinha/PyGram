PYTHON = python

install:
	cat requirements/*.txt > requirements.txt
	pip install -r requirements.txt

	$(PYTHON) setup.py install

test:
	$(PYTHON) setup.py test

run:
	$(PYTHON) -m pygram

clean:
	$(PYTHON) setup.py clean
