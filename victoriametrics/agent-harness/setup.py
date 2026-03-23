from setuptools import setup
setup(
    name='cli-anything-victoriametrics',
    version='1.0.0',
    packages=['cli_anything.victoriametrics'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-victoriametrics=cli_anything.victoriametrics:cli']},
)
