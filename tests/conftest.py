import json
import os
import sys
from configparser import ConfigParser

import jsonschema
import pytest
from faker import Faker
from playwright.sync_api import sync_playwright
from utils.validator import Validator

from app.Browser import chose_browser


def read_ini():
    root_path = os.path.join(sys.path[0], "project-config.ini")
    parser = ConfigParser()
    parser.read(root_path)
    return parser


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="stage",
        help="Chose env to run tests"
    )
    parser.addoption(
        "--browser",
        action="append",
        default=[],
        help='Chose browser to run tests: "chrome", "chromium", "firefox" or "webkit" '
             '(can several)'
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="on/off headless mode"
    )


@pytest.fixture(scope='session')
def base_url(request):
    env_name = request.config.getoption('--env')
    try:
        return read_ini()[env_name]['base_url']
    except KeyError:
        raise Exception(f"Wrong configuration [{env_name}]")


@pytest.fixture(scope='session')
def headless(request) -> bool:
    return request.config.getoption('--headless')


def pytest_generate_tests(metafunc):
    metafunc.parametrize(
        'browser_name',
        metafunc.config.getoption('browser'),
        scope='session'
    )


@pytest.fixture(scope="session")
def browser(headless: bool, browser_name: str):
    with sync_playwright() as p:
        browser = chose_browser(p, browser_name, headless)
        yield browser


@pytest.fixture(scope='function')
def context(browser):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True)
    yield context
    context.tracing.stop(path="trace.zip")
    context.close()


@pytest.fixture(scope='session')
def faker():
    faker = Faker()
    return faker


@pytest.fixture(scope='function')
def fake_login(faker) -> str:
    return faker.first_name()


@pytest.fixture(scope='function')
def fake_password(faker) -> str:
    return faker.password()


@pytest.fixture(scope='session')
def creds_for_login() -> dict:
    try:
        with open(f'{sys.path[0]}/credentials.json', 'r') as file:
            creds = json.load(file)
        Validator.validate_credentials(creds)
        return creds
    except FileNotFoundError:
        raise 'Not found credentials.json. Please, add or create this'


