from setuptools import setup
setup(
    name='cli-anything-q',
    version='1.0.0',
    packages=['cli_anything.q'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-q=cli_anything.q:cli']},
)
