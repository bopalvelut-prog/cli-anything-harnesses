from setuptools import setup
setup(
    name='cli-anything-pyroscope',
    version='1.0.0',
    packages=['cli_anything.pyroscope'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pyroscope=cli_anything.pyroscope:cli']},
)
