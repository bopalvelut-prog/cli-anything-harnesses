from setuptools import setup
setup(
    name='cli-anything-hubspot',
    version='1.0.0',
    packages=['cli_anything.hubspot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hubspot=cli_anything.hubspot:cli']},
)
