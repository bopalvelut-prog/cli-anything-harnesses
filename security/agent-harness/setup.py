from setuptools import setup
setup(
    name='cli-anything-security',
    version='1.0.0',
    packages=['cli_anything.security'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-security=cli_anything.security:cli']},
)
