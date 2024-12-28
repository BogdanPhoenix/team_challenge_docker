# Інструкція до запуску docker compose

## Налаштування віртуальної машини

- Завантажте Oracle Virtual Box з офіційного [сайту](https://www.virtualbox.org/wiki/Downloads).
- Завантажте та встановіть Oracle Virtual Box Extention Pack з офіційного [сайту](https://www.virtualbox.org/wiki/Downloads) та встановіть його за наступною [інструкцією](https://www.youtube.com/watch?v=8NjV23KLmcU).
- Завантажте образ вже створеної віртуальної машини за [посиланням](https://drive.google.com/drive/folders/1lMgwHXwg_KcQE4-55VIR5-QKwprdKoLA?usp=sharing) та імпортуйте її в Oracle Virtual Box ([відео інтсрукція імпорту](https://www.youtube.com/watch?v=PJdsjpZmMMo)).
- Після запуску віртуальної машини увійдіть в неї за допомогою логіна (project_chat) та пароля (0147896325).
- В командному рядку введіть наступну команду, щоб завантажити файли інсталяції docker-compose:
  ````
    git clone --branch main https://github.com/BogdanPhoenix/team_challenge_docker.git
    cd team_challenge_docker
  ````
- Далі виконайте наступну команду, щоб зробити файли з скріптами могли б виконуватися:
  ````
    chmod 754 install.sh update.sh
  ````
- Введіть наступну команду, щоб запустити етап налаштування docker-compose:
  ````
    ./install.sh
  ````
- Зачекайте 3-5 хв та перейдіть в хостову систему, та введіть в браузері наступні URL:
  ````
    <IP_virt_machine>:8080 #frontend
    <IP_virt_machine>:8181 #backend
  ````
  \<IP_virt_machine\> - дану IP-адресу можна побачити при завершенні розгортання Docker контейнерів або в каталозі проекту слід виконати наступну команду:
  ````
    python3 ./setting/current_ip.py
  ````

## Підключення до віртуальної машини за допомогою ssh

- Запустити віртуальну машину.
- Зайти в систему під наданим логіном та паролем.
- Після входу на екрані з'явиться інформація про систему. Знайдіть наступний рядок: "IPv4 address for enp0s3:". Запам'ятайте або випишіть надану IP адресу, вона знадобиться щоб підключитися за допомогою ssh.
- Підключитися до віртуальної машини за допомогою ssh:
  - для Windows скористайтеся програмою PuTTY ([інструкція](https://www.youtube.com/watch?v=pWDHUlvcAsg)).
  - для Linux використовуйте наступний шаблон термінальної команди:
  ````
  ssh <login>@<IP_address>
  ````
  замість \<login\> вводите наданий логін користувача;

  замість \<IP_address\> водите IP-адресу віртуальної машини, яку потрібно було запам'ятати раніше.
