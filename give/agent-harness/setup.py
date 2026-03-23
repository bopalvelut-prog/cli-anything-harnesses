from setuptools import setup
setup(
    name='cli-anything-give',
    version='1.0.0',
    packages=['cli_anything.give'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-give=cli_anything.give:cli']},
)
