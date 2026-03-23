from setuptools import setup
setup(
    name='cli-anything-small',
    version='1.0.0',
    packages=['cli_anything.small'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-small=cli_anything.small:cli']},
)
