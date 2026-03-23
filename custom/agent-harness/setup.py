from setuptools import setup
setup(
    name='cli-anything-custom',
    version='1.0.0',
    packages=['cli_anything.custom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-custom=cli_anything.custom:cli']},
)
