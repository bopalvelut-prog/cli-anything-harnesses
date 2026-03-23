from setuptools import setup
setup(
    name='cli-anything-beauty',
    version='1.0.0',
    packages=['cli_anything.beauty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beauty=cli_anything.beauty:cli']},
)
