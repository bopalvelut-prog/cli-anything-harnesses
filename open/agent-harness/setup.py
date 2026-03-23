from setuptools import setup
setup(
    name='cli-anything-open',
    version='1.0.0',
    packages=['cli_anything.open'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-open=cli_anything.open:cli']},
)
