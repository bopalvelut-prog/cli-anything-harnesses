from setuptools import setup
setup(
    name='cli-anything-democratic',
    version='1.0.0',
    packages=['cli_anything.democratic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-democratic=cli_anything.democratic:cli']},
)
