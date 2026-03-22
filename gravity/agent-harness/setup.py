from setuptools import setup
setup(
    name='cli-anything-gravity',
    version='1.0.0',
    packages=['cli_anything.gravity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gravity=cli_anything.gravity:cli']},
)
