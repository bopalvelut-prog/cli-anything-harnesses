from setuptools import setup
setup(
    name='cli-anything-braco7',
    version='1.0.0',
    packages=['cli_anything.braco7'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco7=cli_anything.braco7:cli']},
)
