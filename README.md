# F1. Дек с защитой от ошибок

|                       |Все языки  | Mono C# 5.2.0|
|-----------------------|-----------|--------------|
| Ограничение времени   |1 секунда 	|1 секунда     |
| Ограничение памяти    |  64Mb     | 256Mb        |



Напишите программу моделирующую работу дека, реализовав все указанные здесь методы. 
Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды 
программа должна вывести одну строчку. Возможные команды для программы:


**push_front** - Добавить в начало дека новый элемент. Программа должна вывести **ok**.

__push_back__ - Добавить в конец дека новый элемент. Программа должна вывести **ok**.

**pop_front** - Извлечь из дека первый элемент. Программа должна вывести его значение.

**pop_back** - Извлечь из дека последний элемент. Программа должна вывести его значение.

**front** - Узнать значение первого элемента (не удаляя его). Программа должна вывести его значение.

**back** - Узнать значение последнего элемента (не удаляя его). Программа должна вывести его значение.

**size** - Вывести количество элементов в деке.

**clear** - Очистить дек (удалить из него все элементы) и вывести **ok**.

**exit** - Программа должна вывести **bye** и завершить работу.

Гарантируется, что количество элементов в деке в любой момент не превосходит 100. Перед исполнением операций **pop_front**, **pop_back**, **front**, **back** программа должна проверять, содержится ли в деке хотя бы один элемент. Если во входных данных встречается операция **pop_front**, **pop_back**, **front**, **back**, и при этом дек пуст, то программа должна вместо числового значения вывести строку **error**.
