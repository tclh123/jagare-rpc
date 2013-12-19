nothing:
	@echo "Better make nothing be default"

test: service_stop
	dae venv py.test tests

service:
	dae service serve > tmp/jagare_service.log 2>&1 &

service_stop:
	-@kill -9 `lsof -i:7303 -t` 2> /dev/null
