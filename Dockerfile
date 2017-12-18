from pypy:2

run pip install sqlalchemy
run pip install pillow
run pip install flask
run pip install lxml
run pip install python-docx
run pip install uwsgi

run rm -rf /root/.cache
run rm -rf /root/build

run mkdir -p /root/src
add *.py /root/src/
add *.ini /root/src/

volume ["/root/src/data"]

expose 80

workdir /root/src

cmd uwsgi uwsgi.ini
