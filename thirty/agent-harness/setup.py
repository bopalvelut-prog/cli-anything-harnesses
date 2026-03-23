from setuptools import setup
setup(
    name='cli-anything-thirty',
    version='1.0.0',
    packages=['cli_anything.thirty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thirty=cli_anything.thirty:cli']},
)
