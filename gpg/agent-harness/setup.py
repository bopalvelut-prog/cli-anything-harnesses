from setuptools import setup
setup(
    name='cli-anything-gpg',
    version='1.0.0',
    packages=['cli_anything.gpg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gpg=cli_anything.gpg:cli']},
)
