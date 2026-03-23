from setuptools import setup
setup(
    name='cli-anything-healthcheck',
    version='1.0.0',
    packages=['cli_anything.healthcheck'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-healthcheck=cli_anything.healthcheck:cli']},
)
