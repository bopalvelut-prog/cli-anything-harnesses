from setuptools import setup
setup(
    name='cli-anything-braco3',
    version='1.0.0',
    packages=['cli_anything.braco3'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco3=cli_anything.braco3:cli']},
)
