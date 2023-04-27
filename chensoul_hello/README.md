# chensoul_hello

记录 setuptools 和 build 构建、twine 上传的使用方法

# 操作过程

```bash
python -m venv ~/.venv
source ~/.venv/bin/activate

pip install setuptools
python setup.py sdist bdist_wheel


pip

pip install twine
twine upload dist/* --skip-existing

pip install dist/chensoul_hello-1.0.0.tar.gz
hello_command

pip install chensoul_hello
hello_command

pip install build
python -m build 
twine upload dist/* --skip-existing
```