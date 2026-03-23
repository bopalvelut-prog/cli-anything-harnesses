from setuptools import setup
setup(
    name='cli-anything-humio',
    version='1.0.0',
    packages=['cli_anything.humio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-humio=cli_anything.humio:cli']},
)
