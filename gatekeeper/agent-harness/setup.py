from setuptools import setup
setup(
    name='cli-anything-gatekeeper',
    version='1.0.0',
    packages=['cli_anything.gatekeeper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gatekeeper=cli_anything.gatekeeper:cli']},
)
