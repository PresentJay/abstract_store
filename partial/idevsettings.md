# Initial development Settings

# supporting environments

> 1. virtualenv

```powershell
>> **pip install -y virtualenv**

/* 0. virtualenv 패키지 설치 */
```

```powershell
>> **virtualenv [venv_name]**

/* 1. [venv_name]으로 virtualenv 환경 생성 */
```

```powershell
>> **./[venv_name]/Scripts/activate**

/* 2. [venv_name] 가상환경 실행 */
```

```powershell
>> **pip install -r [requirements_name]**

/* 3. 작성된 requirements.txt의 패키지 전체 설치 */
```

requrements가 없다면? 

pip install로 패키지를 모두 설치한 후
>> *pip freeze > [requirements_name]*
명령어로 만드세요! (확장자 txt)

> 2. pipenv

```powershell
>> **pip install -y pipenv**

/* 0. pipenv 패키지 설치 */
```

```powershell
>> **pipenv --three**

/* 1. pipenv를 python 3버전 환경으로 생성 */
```

```powershell
>> **pipenv shell**

/* 2. pipenv 가상환경 실행 */
```

```powershell
>> **pipenv update**

/* 3. pipenv.lock에 있는 이미 설치된 패키지를 따라 설치함 */
```

pipenv환경에서의 설치는 pip가 아니라, **pipenv install** 입니다!