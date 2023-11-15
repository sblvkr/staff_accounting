<h1 align="center">Staff Accounting</h1>

## Demo
Site: [http://109.107.190.191/](http://109.107.190.191/)

## Tech stack
1. Python 3.11
2. Django 4.2.7
3. Postgres 13
4. Nginx 1.24.0
5. Docker

## Installing and running locally

1. Install [Docker](https://www.docker.com/get-started)

2. Clone the repo

    ```sh
    git clone https://github.com/sblvkr/staff_accounting.git
    cd staff_accounting
    ```

3. Create environment to the example(.env.example).

   For a quick start, you only need to add SECRET_KEY. Use the service [djecrety.ir](https://djecrety.ir/) (or similar) to create it.
   ```sh
    cp .env.example .env
    nano/vim .env
    ```

4. Run

    ```sh
    docker compose -f docker-compose.dev.yml up
    ```

## About me

Kirill Sobolev ([Telegram](https://sblvkr.t.me/), [E-mail](mailto:sblvkr@gmail.com))
