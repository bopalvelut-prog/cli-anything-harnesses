from setuptools import setup
setup(
    name='cli-anything-dream',
    version='1.0.0',
    packages=['cli_anything.dream'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dream=cli_anything.dream:cli']},
)
