from setuptools import setup
setup(
    name='cli-anything-lunchy',
    version='1.0.0',
    packages=['cli_anything.lunchy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lunchy=cli_anything.lunchy:cli']},
)
