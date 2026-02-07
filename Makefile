# Run 'make up' to start the project
up:
	docker compose up --build -d

# Run 'make down' to stop everything
down:
	docker compose down

# Run 'make logs' to see what the API is doing
logs:
	docker compose logs -f api

# Run 'make test' to ping the model
test:
	curl http://localhost:8000/health
