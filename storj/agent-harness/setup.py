from setuptools import setup
setup(
    name='cli-anything-storj',
    version='1.0.0',
    packages=['cli_anything.storj'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-storj=cli_anything.storj:cli']},
)
