from setuptools import setup
setup(
    name='cli-anything-gnupg',
    version='1.0.0',
    packages=['cli_anything.gnupg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gnupg=cli_anything.gnupg:cli']},
)
