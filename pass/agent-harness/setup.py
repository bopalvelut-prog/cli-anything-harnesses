from setuptools import setup
setup(
    name='cli-anything-pass',
    version='1.0.0',
    packages=['cli_anything.pass'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pass=cli_anything.pass:cli']},
)
