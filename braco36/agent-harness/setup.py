from setuptools import setup
setup(
    name='cli-anything-braco36',
    version='1.0.0',
    packages=['cli_anything.braco36'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco36=cli_anything.braco36:cli']},
)
