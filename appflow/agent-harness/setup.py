from setuptools import setup
setup(
    name='cli-anything-appflow',
    version='1.0.0',
    packages=['cli_anything.appflow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-appflow=cli_anything.appflow:cli']},
)
