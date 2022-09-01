# FROM
docker build -t sugengw07/alpine from

#RUN
#pada dasarnya docker akan menggunakan cached dengan image atau instruksi sebelumnya kalau dalam dockerfile tidak ada perubahan
docker build -t sugengw07/apline_run run

#Untuk menampilkan progress dan tidak menggunakan cached bisa dengan argumen --progress=plain --no-cache
docker build -t sugengw07/apline_run run --progress=plain --no-cache

#command
docker build -t sugengw07/command command

docker build -t sugengw07/ignore ignore

docker container create --name ignore sugengw07/ignore
docker container start ignore
docker container logs ignore

docker container stop ignore 
docker container rm ignore

docker image rm ignore