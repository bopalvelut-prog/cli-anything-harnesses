from setuptools import setup
setup(
    name='cli-anything-balena',
    version='1.0.0',
    packages=['cli_anything.balena'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-balena=cli_anything.balena:cli']},
)
