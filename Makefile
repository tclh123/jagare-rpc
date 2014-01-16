targets:
	@echo test, service, service_stop, service_gen, clean_pyc

test: service_stop
	dae venv py.test tests

service:
	dae service serve > tmp/jagare_service.log 2>&1 &

service_stop:
	-@kill -9 `lsof -i:7303 -t` 2> /dev/null

service_gen:
	dae service gen

clean_pyc:
	@find . -name "*.pyc" -exec rm {} +

.PHONY: service_gen
