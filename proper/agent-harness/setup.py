from setuptools import setup
setup(
    name='cli-anything-proper',
    version='1.0.0',
    packages=['cli_anything.proper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-proper=cli_anything.proper:cli']},
)
