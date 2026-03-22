from setuptools import setup
setup(
    name='cli-anything-braco22',
    version='1.0.0',
    packages=['cli_anything.braco22'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco22=cli_anything.braco22:cli']},
)
