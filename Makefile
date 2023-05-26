docker-spin-up:
	docker compose --env-file env up --build -d

sleeper:
	sleep 15

up: docker-spin-up sleeper

down:
	docker compose down

tf-init:
	terraform -chdir=./terraform init

infra-up:
	terraform -chdir=./terraform apply -var-file="terraform.tfvars"

infra-down:
	terraform -chdir=./terraform destroy

db-migration:
	@read -p "Enter migration name:" migration_name; docker exec webserver yoyo new ./migrations -m "$$migration_name"

warehouse-migration:
	docker exec webserver yoyo develop --no-config-file --database postgres://sdeuser:sdepassword1234@warehouse:5432/covid ./migrations
