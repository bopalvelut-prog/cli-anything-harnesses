from setuptools import setup
setup(
    name='cli-anything-beside',
    version='1.0.0',
    packages=['cli_anything.beside'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beside=cli_anything.beside:cli']},
)
