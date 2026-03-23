from setuptools import setup
setup(
    name='cli-anything-deny',
    version='1.0.0',
    packages=['cli_anything.deny'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deny=cli_anything.deny:cli']},
)
