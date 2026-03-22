from setuptools import setup
setup(
    name='cli-anything-braco35',
    version='1.0.0',
    packages=['cli_anything.braco35'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco35=cli_anything.braco35:cli']},
)
