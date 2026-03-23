from setuptools import setup
setup(
    name='cli-anything-sorry',
    version='1.0.0',
    packages=['cli_anything.sorry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sorry=cli_anything.sorry:cli']},
)
