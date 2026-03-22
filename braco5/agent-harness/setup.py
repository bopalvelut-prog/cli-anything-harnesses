from setuptools import setup
setup(
    name='cli-anything-braco5',
    version='1.0.0',
    packages=['cli_anything.braco5'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco5=cli_anything.braco5:cli']},
)
