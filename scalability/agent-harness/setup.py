from setuptools import setup
setup(
    name='cli-anything-scalability',
    version='1.0.0',
    packages=['cli_anything.scalability'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scalability=cli_anything.scalability:cli']},
)
