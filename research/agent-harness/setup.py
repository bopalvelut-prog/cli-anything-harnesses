from setuptools import setup
setup(
    name='cli-anything-research',
    version='1.0.0',
    packages=['cli_anything.research'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-research=cli_anything.research:cli']},
)
