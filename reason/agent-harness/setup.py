from setuptools import setup
setup(
    name='cli-anything-reason',
    version='1.0.0',
    packages=['cli_anything.reason'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reason=cli_anything.reason:cli']},
)
