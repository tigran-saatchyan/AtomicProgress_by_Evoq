<h1 align="center">AtomicProgress by EvoQ</h1>

<h4 align="center">Track and build life-changing habits the atomic way with Atomic Progress Tracker. Start small, achieve big.</h4>

<p align="center">
  <a href="https://github.com/tigran-saatchyan/AtomicProgress_by_EvoQ/blob/master/LICENSE"><img src="https://img.shields.io/github/license/tigran-saatchyan/mailcraft-by-evoq" alt="License"></a>
  <a href="https://t.me/PythonistiC"><img src="https://img.shields.io/badge/telegram-@PythonistiC-blue.svg?logo=telegram" alt="Telegram"></a>
  <a href="https://www.paypal.me/TigranSaatchyan"><img src="https://img.shields.io/badge/support-paypal-blue.svg?logo=paypal" alt="Support me on Paypal"></a>
</p>



<p align="center">
  <img src="https://i.postimg.cc/TP482RW1/img.png" alt="screenshot">
</p>

[![Flake8](https://github.com/tigran-saatchyan/AtomicProgress_by_Evoq/actions/workflows/flake8.yml/badge.svg?branch=develop)](https://github.com/tigran-saatchyan/AtomicProgress_by_Evoq/actions/workflows/flake8.yml)

## Table of Contents

* [Background / Overview](#background--overview)
* [Features](#features)
* [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Setting up](#setting-up)
  * [Structure / Scaffolding](#structure--scaffolding)
* [Documentation](#documentation)
* [Browser Support](#browser-support)
* [Dependencies](#dependencies)
* [Todo](#todo)
* [Release History](#release-history)
* [Changelog](#changelog)
* [Issues](#issues)
* [Bugs](#bugs)
* [Translations](#translations)
* [Authors](#authors)
* [Acknowledgments](#acknowledgments)
* [Support](#support)
* [License](#license)

## Background / Overview

Atomic Progress Tracker is your ultimate companion on the journey to
building life-changing habits inspired by James Clear's
"Atomic Habits." It empowers you to break down your goals into
small, manageable atomic habits. With our intuitive tracking system,
you can monitor your daily progress, gain insights into your habits,
and make consistent improvements over time.

## Features

Certainly, here are the key features for an API-based application in Markdown format:

**1. Atomic Habit Tracking API:**
   - Easily create and track atomic habits in your application.
   - Simplify users' focus on daily improvements.

**2. Progress Insights API:**
   - Access detailed progress reports and analytics data.
   - Offer users valuable insights into their habit-building journeys.

**3. Personalized Guidance API:**
   - Provide users with tailored habit-building recommendations and reminders.
   - Enhance user engagement and goal achievement.

**4. Community Support API:**
   - Connect users with like-minded individuals within your application.
   - Foster community-building, sharing of successes, and collaborative learning.

**5. Achievement Rewards API:**
   - Implement a rewards and badge system within your application.
   - Motivate users by recognizing and celebrating their milestones and achievements.

## Prerequisites

You will need the following installed on your computer.

* [Git](https://git-scm.com/)
* [Python Poetry](https://python-poetry.org/)
* [Redis](https://redis.io/)

### Installation

Open your terminal and type in

[//]: # (TODO: update after composer is implemented)
[//]: # ()
[//]: # (```sh)

[//]: # ($ git clone https://github.com/tigran-saatchyan/AtomicProgress_by_Evoq.git)

[//]: # ($ cd AtomicProgress_by_Evoq)

[//]: # (```)

[//]: # ()
[//]: # (Install all the packages)

[//]: # ()
[//]: # (```sh)

[//]: # ($ poetry shell)

[//]: # ($ poetry install)

[//]: # (```)

Install all the packages

```sh
$ docker build -t atomic_progress .
$ docker run --env-file=.env atomic_progress:latest
```

### Setting up

Run all migrations
```sh
$ python manage.py migrate
```


### Structure / Scaffolding

<details>

<summary>Project Structure</summary>

```text
        Tigran Saatchyan ~ git version 2.34.1
    -------------------------------------
    Project: AtomicProgress_by_EvoQ
    Languages:
               ● Python (97.6 %) ● HTML (2.4 %)

    Authors: 100% Tigran Saatchyan
    URL: git@github.com:tigran-saatchyan/AtomicProgress_by_EvoQ.git
    Commits: 45

    Lines of code: 1690
    Size: 164.57 KiB (69 files)
    License: MIT

AtomicProgress_by_EvoQ
├── common
│  ├── __init__.py
│  ├── constants.py
│  ├── tests.py
│  └── utils
│     └── __init__.py
├── config
│  ├── __init__.py
│  ├── asgi.py
│  ├── celery.py
│  ├── settings.py
│  ├── urls.py
│  └── wsgi.py
├── docs.py
├── fixtures
├── habits
│  ├── __init__.py
│  ├── admin.py
│  ├── apps.py
│  ├── migrations
│  │  ├── 0001_initial.py
│  │  ├── 0002_alter_habit_connected_habit.py
│  │  ├── 0003_alter_habit_options.py
│  │  ├── 0004_alter_habit_reward.py
│  │  └── __init__.py
│  ├── models.py
│  ├── paginators.py
│  ├── serializers.py
│  ├── services.py
│  ├── tasks.py
│  ├── tests.py
│  ├── urls.py
│  └── views.py
├── LICENSE
├── locations
│  ├── __init__.py
│  ├── admin.py
│  ├── apps.py
│  ├── migrations
│  │  ├── 0001_initial.py
│  │  └── __init__.py
│  ├── models.py
│  ├── serializers.py
│  ├── tests.py
│  ├── urls.py
│  └── views.py
├── manage.py
├── media
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.txt
├── static
│  └── readme
│     └── img.png
├── telegram_bot
│  ├── __init__.py
│  ├── bot.py
│  └── user_registration.py
├── TERMS_OF_SERVICE.md
└── users
   ├── __init__.py
   ├── admin.py
   ├── apps.py
   ├── management
   │  ├── __init__.py
   │  └── commands
   │     ├── __init__.py
   │     └── create_su.py
   ├── managers.py
   ├── migrations
   │  ├── 0001_initial.py
   │  ├── 0002_alter_user_is_active.py
   │  ├── 0003_user_telegram_user_id.py
   │  └── __init__.py
   ├── models.py
   ├── serializers.py
   ├── service.py
   ├── tasks.py
   ├── templates
   │  └── users
   │     └── registration
   │        └── verification_email.html
   ├── tests.py
   ├── urls.py
   └── views.py

```

</details>


<strong>Note:</strong> The scaffolding was generated with tree.

## Documentation

  * Create SuperUser
```sh
$ python manage.py create_su
```


## Browser Support

|  Chrome  |  IE  |   Edge   |  Safari  | Firefox  |
| :------: | :--: | :------: | :------: | :------: |
| Latest 2 |  9+  | Latest 2 | Latest 2 | Latest 2 |

## Dependencies

List of dependencies used in the project

| **Main Libraries**                                                                                                                                                                                                                                                                              | **Other Libraries**                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![Python Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2FAtomicProgress_by_Evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.python&style=flat&logo=python&label=Python)                                     | ![Pillow Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2FAtomicProgress_by_Evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.Pillow&style=flat&label=Pillow)                               |
| ![Django Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2FAtomicProgress_by_Evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.Django&style=flat&logo=django&label=Django)                                     | ![psycopg Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2FAtomicProgress_by_Evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.psycopg&style=flat&label=psycopg)                            |
| ![Redis Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2FAtomicProgress_by_Evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.redis&style=flat&logo=redis&label=Redis)                                         | ![Celery Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2FAtomicProgress_by_Evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.celery&style=flat&logo=Celery&label=Celery)                   |
| ![Django-Celery-Beat Badge](https://img.shields.io/badge/Django--Celery--Beat-%5E2.5.0-blue?logo=Django) | ![drf-yasg Badge](https://img.shields.io/badge/drf--yasg-%5E1.21.7-blue?logo=django)                                                                                                                                                                                          |
| ![DRF Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2FAtomicProgress_by_Evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.djangorestframework&style=flat&logo=django&label=DRF)                 | ![django-filter Badge](https://img.shields.io/badge/django--filter-%5E23.3-blue?logo=django)                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                 | ![DRFSimpleJWT Badge](https://img.shields.io/badge/DRFSimpleJWT-%5E5.3.0-blue?logo=django)                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                 | ![requests Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2FAtomicProgress_by_Evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.requests&style=flat&label=requests)                         |
|                                                                                                                                                                                                                                                                                                 | ![pyTelegramBotAPI Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2FAtomicProgress_by_Evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.pytelegrambotapi&style=flat&label=pyTelegramBotAPI) |


## Todo

List of things to fix or add

- [x] Improve README.md

## Release History
Actual version: ![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2FAtomicProgress_by_Evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.version&style=flat&label=Version)

[//]: # (* 0.1.0 - Initial release)

[//]: # (  * Added dependencies compilation)

[//]: # (  * Added readme)


## Changelog

Detailed changes for each release will be documented in the
[release notes](https://github.com/users/tigran-saatchyan/projects/10/views/2).

## Issues

![GitHub issues](https://img.shields.io/github/issues/tigran-saatchyan/AtomicProgress_by_Evoq)
![GitHub closed issues](https://img.shields.io/github/issues-closed/tigran-saatchyan/AtomicProgress_by_Evoq)

Please make sure to read the [Issue Reporting Checklist](https://github.com/tigran-saatchyan/AtomicProgress_by_Evoq/issues?q=is%3Aopen) before opening an issue. Issues not conforming to the guidelines may be closed immediately.

## Bugs

If you have questions, feature requests or a bug you want to report, please click [here](https://github.com/tigran-saatchyan/AtomicProgress_by_Evoq/issues) to file an issue.

[//]: # (## Deployment)

[//]: # ()
[//]: # (Add additional notes about how to deploy this on a live system)

## Translations

* :ru: Russian/Русский

## Authors

* [**Tigran Saatchyan**](https://github.com/tigran-saatchyan) - AtomicProgress by EvoQ

See also the list of [contributors](#acknowledgments) who participated in this project.

## Acknowledgments

This project would not have been possible without the help and advice of many contributors and the tremendous support of each of you.

## Contact Us:

  * Discord: ![Discord](https://img.shields.io/discord/1152575327810363482)

## Support

Like what you see? Keep me awake at night by buying me a coffee or two.

<a href="https://www.buymeacoffee.com/saatchyan" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Book" style="height: 60px !important;width: 217px !important;" ></a>

## License
Copyright (c) 2023 Tigran Saatchyan.

Usage is provided under the MIT License. See [LICENSE](https://github.com/tigran-saatchyan/CogniVerse_by_EvoQ/blob/master/LICENSE) for the full details.
