from setuptools import setup
setup(
    name='cli-anything-synergy',
    version='1.0.0',
    packages=['cli_anything.synergy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-synergy=cli_anything.synergy:cli']},
)
