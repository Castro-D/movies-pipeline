docker-spin-up:
	docker compose --env-file env up --build -d

sleeper:
	sleep 15

up: docker-spin-up sleeper warehouse-migration

down:
	docker compose down

####################################################################################################################
# Set up cloud infrastructure

tf-init:
	terraform -chdir=./terraform init

infra-up:
	terraform -chdir=./terraform apply -var-file="terraform.tfvars"

infra-down:
	terraform -chdir=./terraform destroy

####################################################################################################################
# Datawarehouse migration

db-migration:
	@read -p "Enter migration name:" migration_name; docker exec pipelinerunner yoyo new ./migrations -m "$${migration_name}_$(date +%Y%m%d%H%M%S)"

warehouse-migration:
	docker exec pipelinerunner yoyo develop --no-config-file --database postgres://sdeuser:sdepassword1234@warehouse:5432/covid ./migrations

warehouse-rollback:
	docker exec pipelinerunner yoyo rollback --no-config-file --database postgres://sdeuser:sdepassword1234@warehouse:5432/covid ./migrations

coverage:
	docker exec pipelinerunner pytest --cov=./src/covid tests/

pytest:
	docker exec pipelinerunner pytest /code/tests

format:
	docker exec pipelinerunner python -m black -S --line-length 79 .

isort:
	docker exec pipelinerunner isort .

type:
	docker exec pipelinerunner mypy --ignore-missing-imports /code

lint: 
	docker exec pipelinerunner flake8 /code 

ci: isort format type lint pytest

stop-etl: 
	docker exec pipelinerunner service cron stop