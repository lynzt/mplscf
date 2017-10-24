docker build  -t python/mplscf-scripts .

docker run -it --rm --name mplscf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mplscf:postgres python/mplscf-scripts

docker run -it --rm --name mplscf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mplscf:postgres python/mplscf-scripts python3 ./scripts/get_report.py



create container

docker run -d --name postgres-mplscf -p 5434:5432 -v pg-data:/var/lib/postgresql/data  postgres:latest

docker start  postgres-mplscf

interact w/ psql container
docker exec -it postgres-mplscf /bin/sh

login db...
psql -U postgres





docker pull jbarlow83/ocrmypdf-tess4
docker tag jbarlow83/ocrmypdf-tess4 ocrmypdf
docker run --rm ocrmypdf --help

docker run -v "$PWD:/home/docker" ocrmypdf --sidecar temp6.txt betsy22.pdf temp6.pdf


docker pull kalledk/pdftotext
docker run --rm -i kalledk/pdftotext < temp6.pdf > temp6.txt

docker run --rm -v "${PWD}":/home/docker ocrmypdf/mplscf --deskew --clean --remove-background --tesseract-timeout=0 frey.pdf output.pdf
