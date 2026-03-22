from setuptools import setup
setup(
    name='cli-anything-braco15',
    version='1.0.0',
    packages=['cli_anything.braco15'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco15=cli_anything.braco15:cli']},
)
