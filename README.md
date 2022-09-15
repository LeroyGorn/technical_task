# technical_task

Hello there ! To use my code, you should:
if you want to run without docker:
1) Firstly install packages from requirements.txt
2) Then specify postgres database settings manually in files.
3) After simply load main.py with your IDE or using terminal: "python main.py" command
4) Wait until script finished it work and then you can see all data in your postgres DB :)

OR Use docker-compose:
1) Run: docker-compose up --build
2) Wait until containers up
3) Enter pgadmin via link: localhost:8080 and loging credentials stored in docker_compose.yml 
4) Monitore your DB :)

Tech stack:
requests, sqlalchemy, postgresDB, docker-compose.
Dump file - dump.sql
Main working file - main.py