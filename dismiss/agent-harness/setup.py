from setuptools import setup
setup(
    name='cli-anything-dismiss',
    version='1.0.0',
    packages=['cli_anything.dismiss'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dismiss=cli_anything.dismiss:cli']},
)
