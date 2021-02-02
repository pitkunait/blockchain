run:
	docker build -t blockchain . && docker run -p 5000:5000 blockchain