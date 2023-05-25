docker-spin-up:
	docker compose --env-file env up airflow-init && docker compose --env-file env up --build -d

perms:
	sudo mkdir -p logs plugins temp dags tests migrations && sudo chmod -R u=rwx,g=rwx,o=rwx logs plugins temp dags tests

up: perms docker-spin-up

down:
	docker compose down

tf-init:
	terraform -chdir=./terraform init

infra-up:
	terraform -chdir=./terraform apply -var-file="terraform.tfvars"

infra-down:
	terraform -chdir=./terraform destroy
