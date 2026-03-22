from setuptools import setup
setup(
    name='cli-anything-cisco',
    version='1.0.0',
    packages=['cli_anything.cisco'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cisco=cli_anything.cisco:cli']},
)
