SHELL = /bin/bash
.DEFAULT_GOAL = mysql

DEFAULT_DB_EXT_PORT = 5432
DEFAULT_DB_INT_PORT = 5432
DEFAULT_WEBSERVER_EXT_PORT = 19211
DEFAULT_WEBSERVER_INT_PORT = 19211
DEFAULT_MONITOR_EXT_PORT = 8080
DEFAULT_MONITOR_INT_PORT = 8080

ifndef DB_EXT_PORT
	DB_EXT_PORT = ${DEFAULT_DB_EXT_PORT}
endif

ifndef DB_INT_PORT
	DB_INT_PORT = ${DEFAULT_DB_INT_PORT}
endif

ifndef WEBSERVER_EXT_PORT
	WEBSERVER_EXT_PORT = ${DEFAULT_WEBSERVER_EXT_PORT}
endif

ifndef WEBSERVER_INT_PORT
	WEBSERVER_INT_PORT = ${DEFAULT_WEBSERVER_INT_PORT}
endif

ifndef MONITOR_EXT_PORT
	MONITOR_EXT_PORT = ${DEFAULT_MONITOR_EXT_PORT}
endif

ifndef MONITOR_INT_PORT
	MONITOR_INT_PORT = ${DEFAULT_MONITOR_INT_PORT}
endif

.PHONY: help
# Provide user help for working with this Makefile
help:
	@echo
	@echo "Usage: make <target>"
	@echo "       make <target> [DB_EXT_PORT=<port_0>] [WEBSERVER_EXT_PORT=<port_1>] [MONITOR_EXT_PORT=<port_2>]"
	@echo
	@echo "Example:"
	@echo "       make up DB_EXT_PORT=5431 WEBSERVER_EXT_PORT=19210 MONITOR_EXT_PORT=8079"
	@echo
	@echo "where <target> is one of:"
	@echo "  help         to print this help info"
	@echo "  env          to make the .env envar file used by docker-compose.yml"
	@echo "  sqlite       to configure the system to use SQLite"
	@echo "  mysql        to configure the system to use MySQL"
	@echo "  postgres     to configure the system to use postgres"
	@echo "  up           to bring up the services in docker-compose"
	@echo "  down         to bring down the services in docker-compose"
	@echo "  clean        to remove the web/src and .env files, but leave the web/coalition.ini"

.PHONY: env
# Set up .env file used for docker-compose.yml
env:
	${warning + $@}
	${warning $@: container port map (database): ${DB_EXT_PORT}:${DB_INT_PORT}}
	${warning $@: container port map (webserver): ${WEBSERVER_EXT_PORT}:${WEBSERVER_INT_PORT}}
	${warning $@: container port map (monitor): ${MONITOR_EXT_PORT}:${MONITOR_INT_PORT}}

	@echo 'DB_EXT_PORT='${DB_EXT_PORT} > .env
	@echo 'DB_INT_PORT='${DB_INT_PORT} >> .env
	@echo 'WEBSERVER_EXT_PORT='${WEBSERVER_EXT_PORT} >> .env
	@echo 'WEBSERVER_INT_PORT='${WEBSERVER_INT_PORT} >> .env
	@echo 'MONITOR_EXT_PORT='${MONITOR_EXT_PORT} >> .env
	@echo 'MONITOR_INT_PORT='${MONITOR_INT_PORT} >> .env

.PHONY: sqlite
# Configure a SQLite backend
sqlite: env
	${warning + $@}
	@cp ./_coalition_sqlite.ini ./coalition.ini
	@cp ./_docker-compose-sqlite.yml ./docker-compose.yml
	@cp ./_requirements-sqlite.txt ./requirements.txt

.PHONY: mysql
# Configure a MySQL backend
mysql: env
	${warning + $@}
	@cp ./_coalition_mysql.ini ./coalition.ini
	@cp ./_docker-compose-mysql.yml ./docker-compose.yml
	@cp ./_requirements-mysql.txt ./requirements.txt

.PHONY: postgres
# Configure a Postgres backend
postgres: env
	${warning + $@}
	@cp ./_coalition_postgres.ini ./coalition.ini
	@cp ./_docker-compose-postgres.yml ./docker-compose.yml
	@cp ./_requirements-postgres.txt ./requirements.txt

.PHONY: up
# Start
up: env
	${warning + $@}
	@sudo docker-compose -f ./docker-compose.yml up  -d --remove-orphans

.PHONY: down
down:
	${warning + $@}
	@sudo docker-compose down

.PHONY: clean
clean:
	${warning + $@}
	@rm --force .env

	@# Delete the coalition.ini file only if it is a copy of one of the other .ini templates
	@if [[ $$({ diff --new-file coalition.ini _coalition_mysql.ini | wc -l & diff --new-file coalition.ini _coalition_postgres.ini | wc -l & diff --new-file coalition.ini _coalition_sqlite.ini | wc -l; } | grep '^0$$' | wc -l) = 1 ]]; then rm --force ./coalition.ini && echo Deleting coalition.ini; else echo "$@: Not deleting customized or missing coalition.ini file"; fi

	@# Delete the docker-compose.yml file only if it is a copy of one of the other compose templates
	@if [[ $$({ diff --new-file docker-compose.yml _docker-compose-mysql.yml | wc -l & diff --new-file docker-compose.yml _docker-compose-postgres.yml | wc -l & diff --new-file docker-compose.yml _docker-compose-sqlite.yml | wc -l; } | grep '^0$$' | wc -l) = 1 ]]; then rm --force ./docker-compose.yml && echo Deleting docker-compose.yml; else echo "$@: Not deleting customized or missing docker-compose.yml file"; fi

	@# Delete the requirements.txt file only if it is a copy of one (or more!) of the other _requirements-*.txt files
	@if [[ $$({ diff --new-file requirements.txt _requirements-mysql.txt | wc -l & diff --new-file requirements.txt _requirements-postgres.txt | wc -l & diff --new-file requirements.txt _requirements-sqlite.txt | wc -l; } | grep '^0$$' | wc -l) != 0 ]]; then rm --force ./requirements.txt && echo Deleting requirements.txt; else echo "$@: Not deleting customized or missing requirements.txt file"; fi

.PHONY: nuke
nuke:
	@echo "+ $@"
	@rm ./coalition.ini 2> /dev/null || true
	@rm ./docker-compose.yml 2> /dev/null || true
	@rm ./requirements.txt 2> /dev/null || true
	@rm ./.env 2> /dev/null || true
