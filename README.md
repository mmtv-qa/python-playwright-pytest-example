Simple UI test automating framework based on Playwright. As platform used website https://www.saucedemo.com/. Unfortunately, this website proved bad to work with network, but enough to demonstrate E2E UI tests with Playwright

How to start:
- Clone repository: *git clone (https/ssh path)*
- Create virtual env: *https://docs.python.org/3/library/venv.html*
- Install requirements: *pip install -r requirements.txt*
- Run tests: *pytest --browser=chrome*

Optional:
- For generate allure report install: *https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/*
- For run tests not only on Chrome install playwright browsers: *playwright install*