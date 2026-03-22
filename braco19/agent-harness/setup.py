from setuptools import setup
setup(
    name='cli-anything-braco19',
    version='1.0.0',
    packages=['cli_anything.braco19'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco19=cli_anything.braco19:cli']},
)
