from setuptools import setup
setup(
    name='cli-anything-between',
    version='1.0.0',
    packages=['cli_anything.between'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-between=cli_anything.between:cli']},
)
