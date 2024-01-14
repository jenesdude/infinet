# Тестовое задание

Результаты можно присылать либо ссылкой на github/bitbucket/где-ещё-удобно с решениями задач либо в архиве.

Ответы на общие вопросы оставить в ReadMe.md

В принципе можно тестовое задание и не делать, если времени мало, но хотя бы представить в уме как его сделать и что у вас получилось бы - надо.

На всякий случай:

* всё уметь не обязательно, всему можно научиться со временем
* хотя бы что-то уметь и иметь интерес к этому - это плюс
* незаконченные, но начатые задачи - лучше чем их отсутствие
* если совсем тяжело сделать что-то на предложенном языке программирования - можете сделать на привычном вам
* если вы считаете, что изящнее будет сделать что-то на другом языке программирования - пожалуйста.
* при задачах связанных с программированием вы можете использовать любые известные и удобные вам библиотеки

## Общие вопросы и скриптинг
* В чем отличие MAC-адреса от IP-адреса?
* Что такое юнит-тестирование и чем оно отличается от функционального?
* Напишите команду(в bash), которая сможет найти в текущей директории и всех поддиректориях все файлы больше 100Kbytes,
    с датой последнего изменения старше 29.03.2019 и отсортируйте вывод в лексикографическом порядке
find . -type f -size +100k ! -newermt 2019-03-29 -exec ls -clh {} +


## Работа с текстом

Написать обработчик текста из консоли на примере вывода статуса от Quanta5.

Можно использовать библиотеки специальные для обработки (textfsm) или обычные регулярные выражения.

Сделать в виде консольной утилиты, которой в виде единственной переменной даётся имя файла, откуда брать текст.

Все данные разбирать необязательно, достаточно нескольких.

```
$ processing_status input_status_OCT.txt
STATUS: "connected"
MCS: 3
...
```

Взять ввод из текста в файле - input_status_OCT.txt.
В выводе текст должен быть в кавычках ("), а числовые значения без кавычек.

## Юнит-тестирование(необязательная задача)

Обвязать функцию из файла unit_test/func.c unit-тестами с помощью библиотеки googletest.

Писать на C на этой работе часто не придётся, но полезно понимать, что происходит.

Дополнить CMakeLists.txt запуском тестов, чтобы можно было их запустить.