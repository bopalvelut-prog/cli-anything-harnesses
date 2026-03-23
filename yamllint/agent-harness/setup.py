from setuptools import setup
setup(
    name='cli-anything-yamllint',
    version='1.0.0',
    packages=['cli_anything.yamllint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yamllint=cli_anything.yamllint:cli']},
)
