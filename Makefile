PYTHON = python

install:
	cat requirements/*.txt > requirements.txt
	pip install -r requirements.txt

	$(PYTHON) setup.py install

test:
	$(PYTHON) setup.py test

clean:
	$(PYTHON) setup.py clean
