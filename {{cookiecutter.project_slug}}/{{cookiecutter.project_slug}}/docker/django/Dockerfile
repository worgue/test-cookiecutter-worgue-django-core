FROM python:{{ cookiecutter.python_version }}

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBIAN_FRONTEND noninteractive

# 明示しておく
ENTRYPOINT ["/bin/bash", "-c"]

WORKDIR /{{cookiecutter.project_slug}}

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y curl gettext postgresql-client

ADD . /{{cookiecutter.project_slug}}
RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install --system --dev

RUN python manage.py compilemessages -l en -l ja
RUN python manage.py collectstatic --noinput

# コンテナ軽量化
RUN rm -rf /var/lib/apt/lists/*