from setuptools import setup
setup(
    name='cli-anything-interception',
    version='1.0.0',
    packages=['cli_anything.interception'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-interception=cli_anything.interception:cli']},
)
