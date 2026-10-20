# Sprint_9 — автотесты Foodgram

Три независимых Selenium-теста: регистрация, авторизация, создание рецепта.
Для каждой функциональности выделены класс и модуль в `test`. Page Object
находятся в `pages`, локаторы — в `locators`, тестовые данные — в `data.py`.
Каждый тест получает отдельную сессию браузера и уникального пользователя;
предусловия оформлены фикстурами. Ожидания только явные.

Загрузка изображения использует `Path.resolve(strict=True)` и `send_keys()`.
Для передачи файла из контейнера тестов в удалённый браузер используется
`LocalFileDetector`.

## Локальный Chrome

Требуются Python 3.10+ и Google Chrome.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --clean-alluredir
```

Selenium Manager подбирает ChromeDriver. На этом компьютере в PATH уже есть
старый ChromeDriver 106 для Chrome 155. Чтобы использовать подходящий драйвер,
запускайте тесты без каталога с устаревшим исполняемым файлом:

```bash
PATH=/usr/bin:/bin .venv/bin/pytest --clean-alluredir
```

Другой стенд можно указать через `BASE_URL`.

## Docker Compose и Selenoid на Apple Silicon

Chrome 128 из `selenoid/vnc_chrome` падает под эмуляцией amd64 при создании
сессии: `Unable to receive message from renderer`. Для Mac arm64 добавлена
конфигурация с официальным образом `selenium/standalone-chromium:4.27.0`.
Браузер запускается нативно на arm64; запросы тестов по-прежнему идут через
Selenoid, который создаёт отдельный браузерный контейнер на каждый тест.

```bash
docker pull selenium/standalone-chromium:4.27.0
docker compose -f docker-compose.yml -f docker-compose.arm64.yml up --build --abort-on-container-exit --exit-code-from tests
docker compose -f docker-compose.yml -f docker-compose.arm64.yml down
```

Настройки удалённого браузера находятся в `selenoid/browsers.arm64.json`.
Для Selenium Standalone используется путь `/wd/hub`, для образа Selenoid
Chrome — `/`. Не передавайте `BROWSER_VERSION=128.0` при запуске arm64-варианта:
без этой переменной Selenoid выбирает версию по умолчанию из своего конфига.

## Docker Compose на Linux amd64

Для исходного Chrome-образа сохранён основной конфиг `selenoid/browsers.json`:

```bash
docker pull selenoid/vnc_chrome:128.0
docker compose up --build --abort-on-container-exit --exit-code-from tests
docker compose down
```

Код завершения Compose соответствует результату pytest. Перед тестами
проверяется готовность Selenoid. Все браузерные контейнеры подключаются
к сети `sprint9`. При запущенном Selenoid его статус доступен по адресу
`http://localhost:4444/status`.

## Особенность авторизации учебного стенда

API `POST /api/auth/token/login/` принимает поле с названием `email`, но
фактически проверяет его значение как username. Это подтверждено отдельными
запросами: аккаунт с различающимися email и username не может войти по email,
но входит, если в это поле передать username.

Для положительных сценариев генератор создаёт уникальные аккаунты с
`username == email`. Это допустимые регистрационные данные; регистрация,
авторизация и создание рецепта выполняются настоящими действиями в браузере
против исходного стенда. Ответы сервиса и токены в браузере не подменяются.
Особенность сервера остаётся отдельным дефектом входа для других аккаунтов.

Также исправлены локатор поля времени приготовления и выбор ингредиента
«абрикосы» из выпадающего списка.

## Allure

Результаты записываются в `allure-results`. Локально параметр
`--clean-alluredir` очищает предыдущие результаты. В Docker каталог является
точкой монтирования: скрипт `scripts/run_tests.py` очищает его содержимое,
сохраняя сам каталог. Передавать `--clean-alluredir` в контейнер не нужно.
Для параллельных локального и контейнерного запусков нужны разные каталоги:

```bash
pytest --alluredir=.local-allure-results
```

Каталог контейнерных результатов можно задать через `ALLURE_RESULTS_DIR`.

Для генерации отчёта требуются Node.js и Java 17+:

```bash
npx --yes allure-commandline@2.32.0 generate allure-results --clean -o allure-report
npx --yes allure-commandline@2.32.0 open allure-report
```

На этом Mac Java есть в составе PyCharm; при отсутствии системной Java:

```bash
export JAVA_HOME='/Applications/PyCharm Professional Edition.app/Contents/jbr/Contents/Home'
```

Готовая папка `allure-report` предназначена для сохранения в репозиторий.
Сырые результаты и виртуальное окружение исключены через `.gitignore`.
В отчёте отображаются шаги тестов и предусловий; при ошибке прикладываются
скриншот и HTML, если браузер позволяет их получить.

## Проверка 20 октября 2026

- Локальный Chrome: все три теста прошли.
- Docker Compose → Selenoid → Chromium arm64: все три теста прошли,
  в том числе создание рецепта с передачей изображения в удалённый браузер.
- Ожидания тестов сохранены: переходы между страницами, форма входа,
  кнопка «Выход», карточка рецепта и точное совпадение его названия.
- Allure-отчёт сформирован по успешному контейнерному прогону.
- Полный лог последнего контейнерного запуска: `artifacts/compose-run.log`.

## GitHub Actions

Репозиторий: https://github.com/gorbunov-d/Sprint_9

Workflow `.github/workflows/ci.yml` запускается при push, pull request
или вручную через Actions → Sprint 9 Selenium → Run workflow. Он загружает
Chrome для Selenoid, собирает Docker-образ и запускает все три теста на
Linux amd64. Allure-отчёт сохраняется как артефакт `allure-report`, в том числе
при ошибке тестов. Изменения только README, отчёта и материалов в `artifacts`
не запускают повторные тесты при push.
