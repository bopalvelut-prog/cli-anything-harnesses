from setuptools import setup
setup(
    name='cli-anything-gitiles',
    version='1.0.0',
    packages=['cli_anything.gitiles'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gitiles=cli_anything.gitiles:cli']},
)
