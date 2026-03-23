from setuptools import setup
setup(
    name='cli-anything-resist',
    version='1.0.0',
    packages=['cli_anything.resist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-resist=cli_anything.resist:cli']},
)
