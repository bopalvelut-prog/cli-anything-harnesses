from setuptools import setup
setup(
    name='cli-anything-incron',
    version='1.0.0',
    packages=['cli_anything.incron'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-incron=cli_anything.incron:cli']},
)
