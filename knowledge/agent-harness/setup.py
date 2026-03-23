from setuptools import setup
setup(
    name='cli-anything-knowledge',
    version='1.0.0',
    packages=['cli_anything.knowledge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-knowledge=cli_anything.knowledge:cli']},
)
