[![Python version](https://img.shields.io/badge/Python-3.8.4-green)](https://www.python.org/)
[![Selenium version](https://img.shields.io/badge/selenium-3.141.0-green)](https://www.python.org/)
[![Structlog version](https://img.shields.io/badge/structlog-20.1.0-green)](https://www.python.org/)
[![GitHub issues][issues-shield]][issues-url]
![GitHub repo size](https://img.shields.io/github/languages/code-size/dmitrii1991/vk.com_test)
![GitHub last commit](https://img.shields.io/github/last-commit/dmitrii1991/vk.com_test)
[![GitHub stars][stars-shield]][stars-url]

# ТЕСТИРОВАНИЕ vk.com

https://yadi.sk/i/qxbhIV5CRuOmcQ

## Описание проекта

* реализовано тестирование главной страницы vk.com на присутствие элементов авторизации/регистрации сайта 
* реализовано тестирование механизма авторизации и регистрации при неверном заполнении данных
* поддержка chrome и firefox
* тесты имеют 2 маркера
  * **title_vk** - проверка элементов, размещенных на главной странице
  * **login_guest** - проверка механизма регистрации/авторизации
* По умолчанию используется chrome, если нужен другой браузер пропишите  **--browser_name firefox** в команде **pytest**
* В проекте есть логгирование в **.log** в виде json
* **ВНИМАНИЕ** если будет вылазить капча - нужно проходить ее вручную. Программа сама определить когда капча пройдена и продолжит тест
* **ВНИМАНИЕ** из коробки настроен интрефейс vk.com на ангийском языке по умолчанию, при смене языка некоторые тесты не завершаться успешно
* можно посмотреть видео работы программы [отcюда](https://yadi.sk/i/qxbhIV5CRuOmcQ) 

## Подготовка к запуску

* нужно установить драйверы для firefox/chrome [отcюда](https://pypi.org/project/selenium/4.0.0a6.post1/) - разместить в 
корневой папке проекта **geckodriver.exe/chromedriver.exe**
* установить необходимые модули и зависимости
```shell script
    pip install -r requirements.txt
```

## запуск тестов
```shell script
    cd nameproject

    # запуск всех тестов
    pytest -v 
    # запуск теста с определенном маркером
    pytest -v -m login_guest
    # запуск теста с определенном маркером в браузере title_vk
    pytest --browser_name firefox -v -m title_vk

```

## Описания тестов для ручного прохождения

### test_guest_can_see_login_elements 
* присутствую элементы 
  * поле ввода телефона/почты для авторизации
  * поле ввода пароля для авторизации
  * кнопка "log in"
  
### test_guest_can_see_register_elements 
* присутствую элементы 
  * поле ввода имени для регистрации
  * поле ввода фамилии для регистрации
  * поля ввода даты/месяца/года для регистрации
  * radio элементы выбора пола для регистрации
  * кнопка "continue registration"
  

### test_guest_can_login 
* провести следущий порядок действий
  * внести любой телефон в поле ввода телефона/почты для авторизации
  * внести любой пароль в поле ввода пароля для авторизации
  * пройти капчу (если появиться)
  * получить сообщение о провале авторизации

### test_guest_can_register 
* провести следущий порядок действий
  * внести любое имя в поле ввода имени для регистрации
  * внести любую фамилию в поле ввода имени для регистрации
  * выбрать любую дату
  * выбрать любой пол
  * нажать на кнопку - продолжить регистрацию
  * пройти капчу (если появиться)
  * внести любой телефон
  * нажать кнопку - получить пароль
  * пройти капчу (если появиться)
  * внести лбой 4-х значный код
  * получить сообщение о провале регистрации


[stars-shield]: https://img.shields.io/github/stars/dmitrii1991/vk.com_test?style=social
[stars-url]: https://github.com/dmitrii1991/com_test/stargazers

[issues-shield]: https://img.shields.io/github/issues/dmitrii1991/vk.com_test
[issues-url]: https://github.com/dmitrii1991/vk.com_test/issues
