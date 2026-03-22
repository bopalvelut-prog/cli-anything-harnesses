from setuptools import setup
setup(
    name='cli-anything-braco12',
    version='1.0.0',
    packages=['cli_anything.braco12'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco12=cli_anything.braco12:cli']},
)
