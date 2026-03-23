from setuptools import setup
setup(
    name='cli-anything-response',
    version='1.0.0',
    packages=['cli_anything.response'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-response=cli_anything.response:cli']},
)
