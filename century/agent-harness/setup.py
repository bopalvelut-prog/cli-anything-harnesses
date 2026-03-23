from setuptools import setup
setup(
    name='cli-anything-century',
    version='1.0.0',
    packages=['cli_anything.century'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-century=cli_anything.century:cli']},
)
