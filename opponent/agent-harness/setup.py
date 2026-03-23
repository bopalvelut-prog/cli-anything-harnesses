from setuptools import setup
setup(
    name='cli-anything-opponent',
    version='1.0.0',
    packages=['cli_anything.opponent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opponent=cli_anything.opponent:cli']},
)
