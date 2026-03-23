from setuptools import setup
setup(
    name='cli-anything-amazon_lex',
    version='1.0.0',
    packages=['cli_anything.amazon_lex'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_lex=cli_anything.amazon_lex:cli']},
)
