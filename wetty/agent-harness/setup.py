from setuptools import setup
setup(
    name='cli-anything-wetty',
    version='1.0.0',
    packages=['cli_anything.wetty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wetty=cli_anything.wetty:cli']},
)
