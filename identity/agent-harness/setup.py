from setuptools import setup
setup(
    name='cli-anything-identity',
    version='1.0.0',
    packages=['cli_anything.identity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-identity=cli_anything.identity:cli']},
)
