from setuptools import setup
setup(
    name='cli-anything-braco41',
    version='1.0.0',
    packages=['cli_anything.braco41'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco41=cli_anything.braco41:cli']},
)
