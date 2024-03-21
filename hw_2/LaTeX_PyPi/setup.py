from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as file:
    return file.read()


setup(
  name='LaTeX_PyPi',
  version='0.3',
  author='puzyriok',
  author_email='sacrumterra@yandex.ru',
  description='This is the simplest module for working with tables and images in LaTeX',
  long_description=readme(),
  packages=find_packages(),
  python_requires='>=3.8'
)