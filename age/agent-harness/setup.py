from setuptools import setup
setup(
    name='cli-anything-age',
    version='1.0.0',
    packages=['cli_anything.age'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-age=cli_anything.age:cli']},
)
