# Infinite Jumps II: Suspicious binaries: Write-up

Прыгаем в __Assembly-CSharp.dll__ (infinite_jumps_Data/Managed)
Видим частично обфусцированный код, но не пугаемся - зашифрованы лишь некоторые переменные и строки.

Видим дерево всех классов.

(фото)

Постепенно доходим до класса `MenuManager` и замечаем строки типа 
```
Debug.LogWarning([1-6]: "some strange data");
```
(фоточка)

Последняя строка намекает на Base64
```
Debug.LogWarning("6:  k3NWY0MzBmODM3dmZ5Mzc1OWYyM3Y=");
```

Соединяем все части флага воедино и декодим

Флаг: **ugra_flag2_unity3ng1n3_decompilation_1s_3asy**

P.S. ПоНрАВиЛасЬ иГрА?
ПиШи СюДА: pirotexnic27@yandex.ru