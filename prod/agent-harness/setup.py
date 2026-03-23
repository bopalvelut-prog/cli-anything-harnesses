from setuptools import setup
setup(
    name='cli-anything-prod',
    version='1.0.0',
    packages=['cli_anything.prod'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prod=cli_anything.prod:cli']},
)
