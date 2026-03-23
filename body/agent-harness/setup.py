from setuptools import setup
setup(
    name='cli-anything-body',
    version='1.0.0',
    packages=['cli_anything.body'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-body=cli_anything.body:cli']},
)
