from setuptools import setup
setup(
    name='cli-anything-braco24',
    version='1.0.0',
    packages=['cli_anything.braco24'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco24=cli_anything.braco24:cli']},
)
