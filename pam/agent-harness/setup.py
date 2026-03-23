from setuptools import setup
setup(
    name='cli-anything-pam',
    version='1.0.0',
    packages=['cli_anything.pam'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pam=cli_anything.pam:cli']},
)
