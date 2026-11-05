
deploy:
	ssh_password=$$(grep '^SSH_PASSWORD=' .env | cut -d '=' -f2- | tr -d '"'); \
	ssh_user=$$(grep '^SSH_USER=' .env | cut -d '=' -f2- | tr -d '"'); \
	ssh_ip=$$(grep '^SSH_IP=' .env | cut -d '=' -f2- | tr -d '"'); \
	sshpass -p "$$ssh_password" ssh "$$ssh_user@$$ssh_ip" "sh ~/deploy.sh"

dev-up:
	docker compose -f docker-compose-dev.yml up -d

dev-down:
	docker compose -f docker-compose-dev.yml down
