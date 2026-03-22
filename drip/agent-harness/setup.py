from setuptools import setup
setup(
    name='cli-anything-drip',
    version='1.0.0',
    packages=['cli_anything.drip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-drip=cli_anything.drip:cli']},
)
