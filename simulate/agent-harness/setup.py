from setuptools import setup
setup(
    name='cli-anything-simulate',
    version='1.0.0',
    packages=['cli_anything.simulate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-simulate=cli_anything.simulate:cli']},
)
