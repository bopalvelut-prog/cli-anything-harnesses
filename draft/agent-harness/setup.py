from setuptools import setup
setup(
    name='cli-anything-draft',
    version='1.0.0',
    packages=['cli_anything.draft'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-draft=cli_anything.draft:cli']},
)
