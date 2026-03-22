from setuptools import setup
setup(
    name='cli-anything-checkov',
    version='1.0.0',
    packages=['cli_anything.checkov'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-checkov=cli_anything.checkov:cli']},
)
