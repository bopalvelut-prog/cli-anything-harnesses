from setuptools import setup
setup(
    name='cli-anything-wasp',
    version='1.0.0',
    packages=['cli_anything.wasp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wasp=cli_anything.wasp:cli']},
)
