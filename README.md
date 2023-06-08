# Test_Work1
## This is simple API APP.

For start app need install Docker, Python > 3.9.
## Deploying APP
After cloning repository, go in it.

`cd c:\\code_directory\`

`cd /code_directory/`

Use **Docker-Compose** for creating *container*.

`docker-compose build`

After building container, will start it.

`docker-compose up`

# EXAMPLE
For requesting data, use POST request in
`{host}/api/{int}` example `http://localhost:8448/api/1`

Request response looks like `[{"id_question":INT,"question":STR,"answer":STR,"date_create":STR}]`

### EXAMPLE RESPONSE

Example of a valid request

`[{"id_question":108883,"question":"Tired of eating mule jerky, Vicksburg fell in July 1863 after a 6-week one of these military tactics","answer":"a siege","date_create":"2022-12-30T19:38:52.192Z"}]`

Example of an erroneous response

`{"detail":[{"loc":["path","questions_num"],"msg":"value is not a valid integer","type":"type_error.integer"}]}`
