from setuptools import setup
setup(
    name='cli-anything-braco46',
    version='1.0.0',
    packages=['cli_anything.braco46'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco46=cli_anything.braco46:cli']},
)
