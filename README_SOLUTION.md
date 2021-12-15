# backend-project-template            

## Hello World
Hello! This is the solution of the test !


### Set-up the enviroment!

For linux: 

docker build `docker-compose -f docker-compose.yml build `.Command to buid each image 
docker up    `docker-compose -f docker-compose.yml up -d`. Command to up the services 
docker logs  `docker-compose -f docker-compose.yml.yml logs -f --tail 100` Command to see the logs 

I run : `sudo docker-compose run --rm directory python mysite/manage.py makemigrations`
and: `sudo docker-compose run --rm directory python mysite/manage.py migrate`

I created a super user using the command:
manage.py createsuperuser: `sudo docker-compose run --rm directory python mysite/manage.py createsuperuser`

The super user was :   username: admin 
                       email: admin@user.com
                       password: 263721aaA*  


### EndPoints

1) here we get the token authentication `localhost:8001/api/auth/` POST_METHOD
    {
    "username": "admin",
    "password": "263721aaA*" 
    }

2) here we get the users `localhost:8001/api/users/`   GET_METHOD

3) here we get the users related to a company `localhost:8001/api/user/company/3`   GET_METHOD

4) Here we've created a hierarchy tree with the created users_report_to
admin is admin 

a) with this endpoint we get the report `localhost:8001/api/user/reports_to/<id:id_reports_to>` 

id_reports_to: provide the id of the users in the head

->return all reports _down_ the reporting tree,


b) with this endpoint we get the report inverse  `localhost:8001/api/user/reports_to_inv/<id:id_reports_to>` 

$        alejocor:
$            marinaber:
$                frodo
$                paquita                
$            julymar: 
$                miamart
$                pachou






curl -X GET http://127.0.0.1:8001/api/users/ -H 'Authorization: Token 051caa97d307db14a8cba96e2d282058f1c29565'

### extras
- I registered in admin.py the model to vizualize it in the admin panel 



