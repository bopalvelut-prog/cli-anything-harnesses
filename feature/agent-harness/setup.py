from setuptools import setup
setup(
    name='cli-anything-feature',
    version='1.0.0',
    packages=['cli_anything.feature'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-feature=cli_anything.feature:cli']},
)
