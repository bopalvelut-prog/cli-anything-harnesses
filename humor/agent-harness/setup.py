from setuptools import setup
setup(
    name='cli-anything-humor',
    version='1.0.0',
    packages=['cli_anything.humor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-humor=cli_anything.humor:cli']},
)
