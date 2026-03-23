from setuptools import setup
setup(
    name='cli-anything-ensure',
    version='1.0.0',
    packages=['cli_anything.ensure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ensure=cli_anything.ensure:cli']},
)
