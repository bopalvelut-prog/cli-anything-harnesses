from setuptools import setup
setup(
    name='cli-anything-sdk',
    version='1.0.0',
    packages=['cli_anything.sdk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sdk=cli_anything.sdk:cli']},
)
