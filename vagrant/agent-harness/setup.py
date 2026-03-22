from setuptools import setup
setup(
    name='cli-anything-vagrant',
    version='1.0.0',
    packages=['cli_anything.vagrant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vagrant=cli_anything.vagrant:cli']},
)
