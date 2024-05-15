# HairWings
사용자에게 헤어스타일을 소개해주고 자기 지역/ 혹은 찾는 지역을 검색하면 주위의 헤어샵을 소개해주는 웹

---

서버 실행 방법
---

가상환경이 설치 안되어있을 경우


- Windows
  
  python-m venv [가상환경이름]
- macOS
  
  python3-m venv [가상환경이름]
 
---
가상환경 실행

- Windows
 
  source [가상환경이름]/Scripts/activate
- macOS
  
  source [가상환경이름]/bin/activate   ```가상환경 끄기 : deactivate```

  
---
Django 설치

pip install django

---
설치후 (manage.py 가 있는 위치에서 실행)

- python manage.py makemigrations ( mac일 경우 python3)
- python manage.py migrate ( mac일 경우 python3)
- python manage.py runserver


