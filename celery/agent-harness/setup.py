from setuptools import setup
setup(
    name='cli-anything-celery',
    version='1.0.0',
    packages=['cli_anything.celery'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-celery=cli_anything.celery:cli']},
)
