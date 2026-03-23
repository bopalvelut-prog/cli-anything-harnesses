from setuptools import setup
setup(
    name='cli-anything-lark',
    version='1.0.0',
    packages=['cli_anything.lark'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lark=cli_anything.lark:cli']},
)
