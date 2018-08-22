all:
	rm -rf output
	npm install
	mkdir -p output
	mkdir -p output/js
	mkdir -p output/css
	cp node_modules/bootstrap/dist/js/bootstrap.min.js output/js/
	cp node_modules/bootstrap/dist/css/bootstrap.min.css output/css/
	cp node_modules/jquery/dist/jquery.min.js output/js/
	python bin/gen_webpage.py
	python bin/gen_volume.py 19
	cp -r img/ output/
	cp -r css/ output/

test:
	! html_lint.py --disable=entities output/beta/*.html | grep Error

develop:
	python -m http.server 8001 --directory output

upload:
	python bin/upload.py
