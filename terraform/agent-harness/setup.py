from setuptools import setup
setup(
    name='cli-anything-terraform',
    version='1.0.0',
    packages=['cli_anything.terraform'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-terraform=cli_anything.terraform:cli']},
)
