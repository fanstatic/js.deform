
version = 3.5
python = python$(version)

test: bin/py.test
	bin/py.test -q

bin/py.test: .pip.log *.py *.cfg
	bin/pip install -e ".[testing]"
	@touch $@

.pip.log: bin/python
	bin/pip install -e "." --log .pip.log

bin/python:
	pyvenv-$(version) .
	@touch $@

clean:
	@rm -rfv bin/ include/ lib/ share/ .Python

.PHONY: test clean
