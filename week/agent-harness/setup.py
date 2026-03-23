from setuptools import setup
setup(
    name='cli-anything-week',
    version='1.0.0',
    packages=['cli_anything.week'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-week=cli_anything.week:cli']},
)
