# OLX Parser Test Assignment

## Development
1) Make a copy of `.env.example` file and rename it to `dev.env`
2) Run `docker-compose -f docker-compose-dev.yml up -d`
3) Run `docker-compose -f docker-compose-dev.yml exec api alembic upgrade head` to run all migrations
4) Go to `localhost:8001/docs`

## Production
1) Make a copy of `.env.example` file and rename it to `prod.env`
2) Fill all needed ENV variables inside `prod.env` with your values
3) Run `docker-compose -f docker-compose.yml up -d`
4) Run `docker-compose -f docker-compose.yml exec api alembic upgrade head` to run all migrations
5) Set up proxy_rules using any proxy server
5) Go to `your_vps_ip/docs`