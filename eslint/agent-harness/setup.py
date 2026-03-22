from setuptools import setup
setup(
    name='cli-anything-eslint',
    version='1.0.0',
    packages=['cli_anything.eslint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-eslint=cli_anything.eslint:cli']},
)
