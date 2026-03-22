from setuptools import setup
setup(
    name='cli-anything-airflow',
    version='1.0.0',
    packages=['cli_anything.airflow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-airflow=cli_anything.airflow:cli']},
)
