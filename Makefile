version = 3.5
python = python$(version)

test-all: bin/py.test
	bin/tox

test: bin/py.test
	bin/py.test

bin/py.test: .pip.log *.py *.cfg
	bin/python setup.py dev
	@touch $@

.pip.log: bin/python
	bin/python setup.py develop

bin/python:
	# virtualenv-$(version) .
	pyvenv-$(version) .
	@touch $@

clean:
	@rm -rf bin/ include/ lib/ share/ .Python .tox

.PHONY: test clean
