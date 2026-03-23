from setuptools import setup
setup(
    name='cli-anything-trust',
    version='1.0.0',
    packages=['cli_anything.trust'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trust=cli_anything.trust:cli']},
)
