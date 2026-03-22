from setuptools import setup
setup(
    name='cli-anything-braco2',
    version='1.0.0',
    packages=['cli_anything.braco2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco2=cli_anything.braco2:cli']},
)
