from setuptools import setup
setup(
    name='cli-anything-limit',
    version='1.0.0',
    packages=['cli_anything.limit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-limit=cli_anything.limit:cli']},
)
