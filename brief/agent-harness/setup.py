from setuptools import setup
setup(
    name='cli-anything-brief',
    version='1.0.0',
    packages=['cli_anything.brief'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brief=cli_anything.brief:cli']},
)
