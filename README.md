<div align='center'>

<img src=https://github.com/Cyberuser-hash/katana_WiFicracker/blob/main/photo/wcrack.png alt="логотип" width=800 height= 1000>

<h1>Тестирование безопасности Wi-Fi</h1>
<h4> <span> · </span> <a href="https://github.com/Cyberuser-hash/katana_WiFicracker/blob/master/README.md"> Документация </a> <span> · </span> <a href="https://github.com/Cyberuser-hash/katana_WiFicracker/issues"> Сообщить об ошибке </a> <span> · </span> <a href="https://github.com/Cyberuser-hash/katana_WiFicracker/issues"> Запросить функцию </a> </h4>

</div>

# :notebook_with_decorative_cover: Содержание

- [О проекте](#star2-о-проекте)
- [План развития](#compass-план-развития)
- [Участие в разработке](#wave-участие-в-разработке)
- [Часто задаваемые вопросы](#grey_question-часто-задаваемые-вопросы)
- [Лицензия](#warning-лицензия)
- [Контакты](#handshake-контакты)
- [Благодарности](#gem-благодарности)

## :star2: О проекте

### :camera: Скриншоты

<div align="center"> <a href=""><img src="https://github.com/Cyberuser-hash/katana_WiFicracker/blob/main/photo/clients.png" alt='изображение' width='800'/></a> </div>
<div align="center"> <a href=""><img src="https://github.com/Cyberuser-hash/katana_WiFicracker/blob/main/photo/scan.png" alt='изображение' width='800'/></a> </div>
### :dart: Возможности

- ✓ Сканирование всех доступных Wi-Fi точек доступа
- ✓ Отображение BSSID, каналов, уровня защиты
- ✓ Мониторинг подключенных клиентов к каждой сети
- ✓ Захват WPA/WPA2 handshake для последующего взлома
- ✓ Deauth атака (принудительное отключение клиентов)
- ✓ Автоматический парсинг CSV файлов airodump-ng
- ✓ Цветной ASCII-art интерфейс
- ✓ Сохранение handshake в .pcap формате
- ✓ Поддержка режима мониторинга
- ✓ Выбор сетевого адаптера
- ✓ Многопоточная отправка deauth пакетов

### :art: Цветовая схема
| Цвет | Hex |
| --------------- | ---------------------------------------------------------------- |
| Основной цвет | ![#FF0000](https://via.placeholder.com/10/FF0000?text=+) #FF0000 |
| Вторичный цвет | ![#00FF00](https://via.placeholder.com/10/00FF00?text=+) #00FF00 |
| Акцентный цвет | ![#FFFF00](https://via.placeholder.com/10/FFFF00?text=+) #FFFF00 |
| Цвет текста | ![#36C5F0](https://via.placeholder.com/10/36C5F0?text=+) #36C5F0 |


## :toolbox: Начало работы

### :running: Локальный запуск

Clone the project

```bash
git clone https://github.com/Cyberuser-hash/katana_WiFicracker
```

Выдача прав
```bash
sudo chmod +x install.sh
```
Установка зависимостей
```bash
sudo ./install.sh
```
Запуск
```bash
sudo python3 katana.py
```



## :compass: План развития


* [x] Сканирование WiFi сетей, автоматизация атак, Захват WPA/WPA2 handshake, Deauth атаки, выбор сетевого адаптера, свап в режим мониторинга
* [ ] Поддержка WPA3(Downgrade атаки), Возможности гибкого брутфорса, Поддержка 5GHz сетей, Массовые атаки, поддержка атак на WPS(Pixie dust), поддержка атак на устаревший WEP, Evil Twin атаки(Captive Portal и другие)


## :wave: Про вклад

<a href="https://github.com/Cyberuser-hash/katana_WiFicracker/graphs/contributors"> <img src="https://contrib.rocks/image?repo=Louis3797/awesome-readme-template" /> </a>

Вклад всегда приветствуется!
Способы начала работы описаны в файле `contributing.md`.

## :grey_question: FAQ


- Какой адаптер нужен? Любой WiFi адаптер с поддержкой monitor mode. Рекомендуются: Alfa AWUS036ACH, TP-Link TL-WN722N, Panda PAU06
- Почему не вижу сети? Убедитесь что адаптер в режиме monitor: sudo airmon-ng start wlan0
- Как взломать handshake? Используйте сторонние утилиты (aircrack-ng, hashcat) позже процесс будет автоматизирован
- Работает на Windows? Нет, только Linux. Используйте WSL или виртуальную машину
- Нужны root права? Да, для работы с сетевыми интерфейсами требуется sudo


## :warning: Лицензия

Распространяется под лицензией MIT. Дополнительную информацию см. в файле LICENSE.txt.

## :handshake: Контакты

Anonymous - - igaj01533@gmail.com

Project Link: [https://github.com/Cyberuser-hash/katana_WiFicracker](https://github.com/Cyberuser-hash/katana_WiFicracker)

## :gem: Благодарности

- [Aircrack-ng](https://www.aircrack-ng.org/)
- [Kali Linux]( https://www.kali.org/)
- [Wireshark](https://www.wireshark.org/)
- [Python](https://www.python.org/)
- [GitHub]( https://github.com/)
- Всем вносящим вклад в кибербезопасность
