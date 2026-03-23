from setuptools import setup
setup(
    name='cli-anything-insist',
    version='1.0.0',
    packages=['cli_anything.insist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-insist=cli_anything.insist:cli']},
)
