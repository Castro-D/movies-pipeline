docker-spin-up:
	docker compose --env-file env up airflow-init && docker compose --env-file env up --build -d

perms:
	sudo mkdir -p logs plugins temp dags tests migrations && sudo chmod -R u=rwx,g=rwx,o=rwx logs plugins temp dags tests migrations

up: perms docker-spin-up warehouse-migration

down:
	docker compose down

tf-init:
	terraform -chdir=./terraform init

infra-up:
	terraform -chdir=./terraform apply -var-file="terraform.tfvars"

infra-down:
	terraform -chdir=./terraform destroy

db-migration:
	@read -p "Enter migration name:" migration_name; docker exec webserver yoyo new ./migrations -m "$migration_name"

warehouse-migration:
	docker exec webserver yoyo develop --no-config-file --database postgres://sdeuser:sdepassword1234@warehouse:5432/covid ./migrations
