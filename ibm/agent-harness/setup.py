from setuptools import setup
setup(
    name='cli-anything-ibm',
    version='1.0.0',
    packages=['cli_anything.ibm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ibm=cli_anything.ibm:cli']},
)
