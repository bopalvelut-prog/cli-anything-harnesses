from setuptools import setup
setup(
    name='cli-anything-gear',
    version='1.0.0',
    packages=['cli_anything.gear'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gear=cli_anything.gear:cli']},
)
