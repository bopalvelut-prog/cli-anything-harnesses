from setuptools import setup
setup(
    name='cli-anything-mysqlclient',
    version='1.0.0',
    packages=['cli_anything.mysqlclient'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mysqlclient=cli_anything.mysqlclient:cli']},
)
