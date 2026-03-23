from setuptools import setup
setup(
    name='cli-anything-sponsor',
    version='1.0.0',
    packages=['cli_anything.sponsor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sponsor=cli_anything.sponsor:cli']},
)
