from setuptools import setup
setup(
    name='cli-anything-braco9',
    version='1.0.0',
    packages=['cli_anything.braco9'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco9=cli_anything.braco9:cli']},
)
