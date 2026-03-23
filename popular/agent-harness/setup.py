from setuptools import setup
setup(
    name='cli-anything-popular',
    version='1.0.0',
    packages=['cli_anything.popular'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-popular=cli_anything.popular:cli']},
)
