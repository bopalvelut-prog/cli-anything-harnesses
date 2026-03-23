from setuptools import setup
setup(
    name='cli-anything-commit',
    version='1.0.0',
    packages=['cli_anything.commit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-commit=cli_anything.commit:cli']},
)
