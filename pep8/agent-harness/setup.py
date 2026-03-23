from setuptools import setup
setup(
    name='cli-anything-pep8',
    version='1.0.0',
    packages=['cli_anything.pep8'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pep8=cli_anything.pep8:cli']},
)
