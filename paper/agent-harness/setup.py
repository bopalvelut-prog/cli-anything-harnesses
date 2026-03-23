from setuptools import setup
setup(
    name='cli-anything-paper',
    version='1.0.0',
    packages=['cli_anything.paper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-paper=cli_anything.paper:cli']},
)
