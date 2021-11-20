# WhatsappRaid
![изображение](https://user-images.githubusercontent.com/55328925/142739444-248e53aa-c489-4f3d-a966-fee985ebe0e9.png)

Скрипт подготовлен специально для сайта https://pysoc.ru и <a href = "https://www.youtube.com/channel/UCIb8Y65gN-Pl7m7Dw7Lgb8A">Ютуб канала PyPro</a>
# Русский
Простой спам бот для WhatsApp на Python3. Работает с использованием Selenium
<h4>Инструкция</h4>
<b>Подготовка:</b></br>
На вашем компьютере должен быть установлен Python3
В терминале(или консоле) выполняете следующую команду <br>
<code>pip3 install selenium</code>
<br>
Далее взависимости от вашего браузера(он будет использоваться для рейда) выбираете ссылку из таблицы ниже, переходите на неё и скачиваете необходимый драйвер для
вашей операционной системы<br>
<table class="docutils" border="1">
<colgroup>
<col width="16%">
<col width="84%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Chrome</strong>:</td>
<td><a class="reference external" href="https://sites.google.com/chromium.org/driver/">https://sites.google.com/chromium.org/driver/</a></td>
</tr>
<tr class="row-even"><td><strong>Edge</strong>:</td>
<td><a class="reference external" href="https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/">https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/</a></td>
</tr>
<tr class="row-odd"><td><strong>Firefox</strong>:</td>
<td><a class="reference external" href="https://github.com/mozilla/geckodriver/releases">https://github.com/mozilla/geckodriver/releases</a></td>
</tr>
<tr class="row-even"><td><strong>Safari</strong>:</td>
<td><a class="reference external" href="https://webkit.org/blog/6900/webdriver-support-in-safari-10/">https://webkit.org/blog/6900/webdriver-support-in-safari-10/</a></td>
</tr>
</tbody>
</table><br>
Официальная документация по установке Selenium Driver - https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/ <br>
<q style="color: red;">Рекомендую использовать Firefox так как для других браузеров надо будет немного изменять код.</q><br>
Далее скачиваете файл "raid.py" из данного репозитория и запускаете его, используя Python3.
<br>
<b>Настройки:</b></br>

![изображение](https://user-images.githubusercontent.com/55328925/142739616-40767a25-7b3e-47bf-b200-2676569b4422.png)

Переменные, отвечающие за конфигурацию бота находятся на строках 13 - 17
<br>
<ol>
  <li><b>message</b> - сообщение для спама, если не используется рандомная генерация</li>
  <li><b>gen_random_string</b> - использовать сообщение из предыдущей переменной или генерировать рандомное(False или True соответственно)</li>
  <li><b>random_string_length</b> - Если используется рандомная генерация, то переменная указывает на длину рандомного сообщения, если она равна -1, то длина сообщения рандомная</li>
  <li><b>delay_seconds</b> - интервал между отправкой сообщений в секундах</li>
</ol>
