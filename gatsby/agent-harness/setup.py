from setuptools import setup
setup(
    name='cli-anything-gatsby',
    version='1.0.0',
    packages=['cli_anything.gatsby'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gatsby=cli_anything.gatsby:cli']},
)
