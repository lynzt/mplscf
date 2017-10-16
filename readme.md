docker build  -t python/mplscf-scripts .

docker run -it --rm --name mplscf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mplscf:postgres python/mplscf-scripts

docker run -it --rm --name mplscf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mplscf:postgres python/mplscf-scripts python3 ./scripts/get_report.py



create container

docker run -d --name postgres-mplscf -p 5434:5432 -v pg-data:/var/lib/postgresql/data  postgres:latest

docker start --p 5432:5432  postgres-mplscf

interact w/ psql container
docker exec -it postgres-mplscf /bin/sh

login db...
psql -U postgres

create user/pass
create user mplscf_web password 'mplscf_123';

grant select, insert, update, delete on all tables in schema public to mplscf_web;
grant all on all sequences in schema public to mplscf_web;

CREATE DATABASE mplscf ENCODING 'utf8' TEMPLATE template0;
