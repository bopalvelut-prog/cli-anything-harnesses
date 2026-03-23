from setuptools import setup
setup(
    name='cli-anything-violence',
    version='1.0.0',
    packages=['cli_anything.violence'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-violence=cli_anything.violence:cli']},
)
