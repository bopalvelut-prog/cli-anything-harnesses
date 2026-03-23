from setuptools import setup
setup(
    name='cli-anything-sure',
    version='1.0.0',
    packages=['cli_anything.sure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sure=cli_anything.sure:cli']},
)
