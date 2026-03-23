from setuptools import setup
setup(
    name='cli-anything-whom',
    version='1.0.0',
    packages=['cli_anything.whom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-whom=cli_anything.whom:cli']},
)
