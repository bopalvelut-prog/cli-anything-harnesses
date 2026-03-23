from setuptools import setup
setup(
    name='cli-anything-temporary',
    version='1.0.0',
    packages=['cli_anything.temporary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-temporary=cli_anything.temporary:cli']},
)
