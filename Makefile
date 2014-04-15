targets:
	@echo test, service, service_stop, clean_pyc  # , service_gen

test: service_restart
	# dae venv py.test tests
	py.test tests

service_restart: service_stop service

service:
	python devserver.py > tmp/jagare_service_2.log 2>&1 &

service_stop:
	-@kill -9 `lsof -i:7303 -t` 2> /dev/null

# service_gen:
# 	dae service gen

clean_pyc:
	@find . -name "*.pyc" -exec rm {} +

.PHONY: service_gen
