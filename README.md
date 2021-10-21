## Getting Started with Django + Gunicorn + Nginx Docker-Compose 

( with Swagger(redoc) Tools with sample model(User) )

--- 

## Available Scripts

In the project directory, you can run:

## 1. Install docker and docker-compose (on Linux) 

``` bash
$ chmod 755 docker_install.sh 
$ ./docker_install.sh
```

---

## 2. Run Docker-Compose 
``` bash 
$ (sudo) docker-compose up -d --build    # run Django(binding Gunicorn) & Nginx Server 
$ (sudo) docker-compose down    # Stop docker-compose
```

---

## 3. Check API Info & Swagger(Redoc) URL 

* django-restframework Main URL : [http://localhost/api](http://localhost/api)
* Swagger URL : [http://localhost/swagger](http://localhost/swagger)
* Redoc URL : [http://localhost/redoc](http://localhost/redoc)
