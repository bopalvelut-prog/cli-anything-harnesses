from setuptools import setup
setup(
    name='cli-anything-test',
    version='1.0.0',
    packages=['cli_anything.test'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-test=cli_anything.test:cli']},
)
