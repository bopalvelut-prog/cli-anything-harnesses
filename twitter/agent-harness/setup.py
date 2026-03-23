from setuptools import setup
setup(
    name='cli-anything-twitter',
    version='1.0.0',
    packages=['cli_anything.twitter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-twitter=cli_anything.twitter:cli']},
)
