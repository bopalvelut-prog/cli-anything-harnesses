from setuptools import setup
setup(
    name='cli-anything-risk',
    version='1.0.0',
    packages=['cli_anything.risk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-risk=cli_anything.risk:cli']},
)
