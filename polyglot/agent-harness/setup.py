from setuptools import setup
setup(
    name='cli-anything-polyglot',
    version='1.0.0',
    packages=['cli_anything.polyglot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-polyglot=cli_anything.polyglot:cli']},
)
