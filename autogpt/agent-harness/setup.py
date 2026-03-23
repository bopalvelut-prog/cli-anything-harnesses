from setuptools import setup
setup(
    name='cli-anything-autogpt',
    version='1.0.0',
    packages=['cli_anything.autogpt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autogpt=cli_anything.autogpt:cli']},
)
