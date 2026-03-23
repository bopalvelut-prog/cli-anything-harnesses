from setuptools import setup
setup(
    name='cli-anything-employer',
    version='1.0.0',
    packages=['cli_anything.employer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-employer=cli_anything.employer:cli']},
)
