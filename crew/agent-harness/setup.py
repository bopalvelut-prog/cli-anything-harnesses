from setuptools import setup
setup(
    name='cli-anything-crew',
    version='1.0.0',
    packages=['cli_anything.crew'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crew=cli_anything.crew:cli']},
)
