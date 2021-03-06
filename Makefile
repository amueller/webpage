all:
	rm -rf output
	npm install
	mkdir -p output/beta/js
	mkdir -p output/beta/css
	cp node_modules/bootstrap/dist/js/bootstrap.min.js output/beta/js/
	cp node_modules/bootstrap/dist/css/bootstrap.min.css output/beta/css/
	cp node_modules/jquery/dist/jquery.min.js output/beta/js/
	python src/gen_webpage.py
	python src/gen_volume.py 18
	python src/gen_volume.py 19
	python src/gen_volume.py 20
	cp -r static/img/ output/
	cp -r static/img/ output/beta/
	cp -r static/css/ output/beta/

test:
	py.test -vv src/tests/test.py

develop:
	livereload -p 8001 output/
