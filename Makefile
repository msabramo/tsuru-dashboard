.PHONY: deploy-to-tsuru

clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r test-requirements.txt

test: clean deps
	@coverage run manage.py test
	@coverage report -m
	@flake8 --max-line-length 110 .

run: clean deps
	@DEBUG=true ./manage.py runserver

deploy-to-tsuru:
	./deploy-to-tsuru
