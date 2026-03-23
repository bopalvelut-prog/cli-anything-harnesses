from setuptools import setup
setup(
    name='cli-anything-beyond',
    version='1.0.0',
    packages=['cli_anything.beyond'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beyond=cli_anything.beyond:cli']},
)
