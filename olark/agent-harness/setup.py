from setuptools import setup
setup(
    name='cli-anything-olark',
    version='1.0.0',
    packages=['cli_anything.olark'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-olark=cli_anything.olark:cli']},
)
