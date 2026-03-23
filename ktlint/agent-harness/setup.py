from setuptools import setup
setup(
    name='cli-anything-ktlint',
    version='1.0.0',
    packages=['cli_anything.ktlint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ktlint=cli_anything.ktlint:cli']},
)
