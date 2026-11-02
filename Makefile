
dev-up:
	docker compose -f docker-compose-dev.yml up -d

dev-down:
	docker compose -f docker-compose-dev.yml down

dev-build:
	docker compose -f docker-compose-dev.yml build

dev-restart:
	docker compose -f docker-compose-dev.yml restart

dev-logs:
	docker compose -f docker-compose-dev.yml logs -f