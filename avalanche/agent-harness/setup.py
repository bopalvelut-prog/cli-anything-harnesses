from setuptools import setup
setup(
    name='cli-anything-avalanche',
    version='1.0.0',
    packages=['cli_anything.avalanche'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-avalanche=cli_anything.avalanche:cli']},
)
