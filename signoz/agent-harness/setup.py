from setuptools import setup
setup(
    name='cli-anything-signoz',
    version='1.0.0',
    packages=['cli_anything.signoz'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-signoz=cli_anything.signoz:cli']},
)
