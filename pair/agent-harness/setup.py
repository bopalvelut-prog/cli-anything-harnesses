from setuptools import setup
setup(
    name='cli-anything-pair',
    version='1.0.0',
    packages=['cli_anything.pair'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pair=cli_anything.pair:cli']},
)
