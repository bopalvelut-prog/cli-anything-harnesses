from setuptools import setup
setup(
    name='cli-anything-grant',
    version='1.0.0',
    packages=['cli_anything.grant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grant=cli_anything.grant:cli']},
)
