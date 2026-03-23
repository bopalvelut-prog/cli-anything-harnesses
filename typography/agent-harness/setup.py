from setuptools import setup
setup(
    name='cli-anything-typography',
    version='1.0.0',
    packages=['cli_anything.typography'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-typography=cli_anything.typography:cli']},
)
