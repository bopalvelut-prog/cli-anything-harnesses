from setuptools import setup
setup(
    name='cli-anything-behind',
    version='1.0.0',
    packages=['cli_anything.behind'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-behind=cli_anything.behind:cli']},
)
