from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()


setup(name='project_timer',
    version='0.0.1',
    license='MIT License',
    author='Edson Rafael',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='edsonrafael2@gmail.com',
    keywords='timer',
    description=u'Um repositorio apenas para efeito de teste, não ofocial',
    packages=['timer_module'],
    install_requires=['time'],)