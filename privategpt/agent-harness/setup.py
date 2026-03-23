from setuptools import setup
setup(
    name='cli-anything-privategpt',
    version='1.0.0',
    packages=['cli_anything.privategpt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-privategpt=cli_anything.privategpt:cli']},
)
