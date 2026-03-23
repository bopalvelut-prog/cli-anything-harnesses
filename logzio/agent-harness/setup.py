from setuptools import setup
setup(
    name='cli-anything-logzio',
    version='1.0.0',
    packages=['cli_anything.logzio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-logzio=cli_anything.logzio:cli']},
)
