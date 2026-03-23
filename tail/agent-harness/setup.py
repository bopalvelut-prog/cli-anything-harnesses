from setuptools import setup
setup(
    name='cli-anything-tail',
    version='1.0.0',
    packages=['cli_anything.tail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tail=cli_anything.tail:cli']},
)
