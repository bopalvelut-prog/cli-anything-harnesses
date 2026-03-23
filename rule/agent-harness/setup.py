from setuptools import setup
setup(
    name='cli-anything-rule',
    version='1.0.0',
    packages=['cli_anything.rule'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rule=cli_anything.rule:cli']},
)
