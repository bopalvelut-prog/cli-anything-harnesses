from setuptools import setup
setup(
    name='cli-anything-asio',
    version='1.0.0',
    packages=['cli_anything.asio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-asio=cli_anything.asio:cli']},
)
