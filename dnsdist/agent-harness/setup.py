from setuptools import setup
setup(
    name='cli-anything-dnsdist',
    version='1.0.0',
    packages=['cli_anything.dnsdist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dnsdist=cli_anything.dnsdist:cli']},
)
