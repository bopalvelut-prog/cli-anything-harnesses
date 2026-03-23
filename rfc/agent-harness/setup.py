from setuptools import setup
setup(
    name='cli-anything-rfc',
    version='1.0.0',
    packages=['cli_anything.rfc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rfc=cli_anything.rfc:cli']},
)
