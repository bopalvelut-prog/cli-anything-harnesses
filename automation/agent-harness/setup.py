from setuptools import setup
setup(
    name='cli-anything-automation',
    version='1.0.0',
    packages=['cli_anything.automation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-automation=cli_anything.automation:cli']},
)
