from setuptools import setup
setup(
    name='cli-anything-authy',
    version='1.0.0',
    packages=['cli_anything.authy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-authy=cli_anything.authy:cli']},
)
