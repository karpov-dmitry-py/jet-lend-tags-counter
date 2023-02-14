.PHONY: .run
.run:
	docker-compose build --no-cache
	docker-compose up -d

.PHONY: .kill
.kill:
	docker-compose down --volumes && docker network prune --force

.PHONY: .log
.log:
	docker-compose logs app

run: .run

kill: .kill

log: .log