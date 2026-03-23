from setuptools import setup
setup(
    name='cli-anything-authority',
    version='1.0.0',
    packages=['cli_anything.authority'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-authority=cli_anything.authority:cli']},
)
