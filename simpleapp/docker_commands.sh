# prefix commands with sudo if user is not in docker group
# build docker image
docker build -t myapp .

# check docker image
docker images | grep myapp

# run docker container
docker run -p 8888:5000 --rm --name myapp myapp 
