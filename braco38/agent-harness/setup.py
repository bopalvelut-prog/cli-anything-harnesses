from setuptools import setup
setup(
    name='cli-anything-braco38',
    version='1.0.0',
    packages=['cli_anything.braco38'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco38=cli_anything.braco38:cli']},
)
