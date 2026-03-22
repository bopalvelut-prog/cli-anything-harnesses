from setuptools import setup
setup(
    name='cli-anything-telegram',
    version='1.0.0',
    packages=['cli_anything.telegram'],
    install_requires=['click', 'requests'],
    entry_points={'console_scripts': ['cli-anything-telegram=cli_anything.telegram:cli']},
)
