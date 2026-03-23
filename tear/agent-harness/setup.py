from setuptools import setup
setup(
    name='cli-anything-tear',
    version='1.0.0',
    packages=['cli_anything.tear'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tear=cli_anything.tear:cli']},
)
