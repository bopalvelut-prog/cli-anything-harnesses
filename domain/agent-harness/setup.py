from setuptools import setup
setup(
    name='cli-anything-domain',
    version='1.0.0',
    packages=['cli_anything.domain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-domain=cli_anything.domain:cli']},
)
