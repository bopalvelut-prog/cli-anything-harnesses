from setuptools import setup
setup(
    name='cli-anything-six',
    version='1.0.0',
    packages=['cli_anything.six'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-six=cli_anything.six:cli']},
)
