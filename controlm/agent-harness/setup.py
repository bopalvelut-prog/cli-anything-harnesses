from setuptools import setup
setup(
    name='cli-anything-controlm',
    version='1.0.0',
    packages=['cli_anything.controlm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-controlm=cli_anything.controlm:cli']},
)
