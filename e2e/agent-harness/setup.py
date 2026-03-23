from setuptools import setup
setup(
    name='cli-anything-e2e',
    version='1.0.0',
    packages=['cli_anything.e2e'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-e2e=cli_anything.e2e:cli']},
)
