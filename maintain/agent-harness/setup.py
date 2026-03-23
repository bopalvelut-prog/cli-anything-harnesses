from setuptools import setup
setup(
    name='cli-anything-maintain',
    version='1.0.0',
    packages=['cli_anything.maintain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-maintain=cli_anything.maintain:cli']},
)
