# Shakespeare: Write-up

Видим, что текст непонятный и довольно длинный. Если зашифрованный текст достаточно длинный, то, в большинстве случаев, его можно расшифровать, просто проведя частотный анализ.
Есть множество удобных онлайн-сервисов для таких задач, например, [этот](https://www.guballa.de/substitution-solver).
Дешифруем текст с помощью частотного анализа и получаем что-то такое:
```
ccdwhen my love swears that she is made of truth, 
ddci do believe her, though i know she lies, 
cdcthat she might think me some untutor'd youth, 
cdunskilful in the world's false forgeries. 
ddthus vainly thinking that she thinks me young, 
cdalthough i know my years be past the best, 
dcci smiling credit her false-speaking tongue, 
cddcoutfacing faults in love with love's ill rest. 
dddbut wherefore says my love that she is young? 
cand wherefore say not i that i am old? 
do, love's best habit is a soothing tongue, 
cdcand age, in love, loves not to have years told. 
dcddtherefore i'll lie with love, and love with me...
```
Получившиеся осмысленные слова говорят о том, что текст дешифрован коректно. Однако в начале нескольких первых строк присутствуют буквы `c` и `d`. Выпишем их:
```
ccd ddc cdc cd dd cd dcc cddc ddd c d cdc dcdd
```
Можно заметить, что если заменить `c` на точку, а `d` - на тире, получившийся текст будет кодом Морзе:
```
..- --. .-. .- -- .- -.. .--. --- . - .-. -.--
```
Переводим код Морзе в текст и получаем флаг.

Флаг: **ugramadpoetry**
