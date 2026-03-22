from setuptools import setup
setup(
    name='cli-anything-braco37',
    version='1.0.0',
    packages=['cli_anything.braco37'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco37=cli_anything.braco37:cli']},
)
