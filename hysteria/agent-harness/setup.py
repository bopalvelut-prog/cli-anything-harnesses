from setuptools import setup
setup(
    name='cli-anything-hysteria',
    version='1.0.0',
    packages=['cli_anything.hysteria'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hysteria=cli_anything.hysteria:cli']},
)
