from setuptools import setup
setup(
    name='cli-anything-common',
    version='1.0.0',
    packages=['cli_anything.common'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-common=cli_anything.common:cli']},
)
