from setuptools import setup
setup(
    name='cli-anything-ascii',
    version='1.0.0',
    packages=['cli_anything.ascii'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ascii=cli_anything.ascii:cli']},
)
