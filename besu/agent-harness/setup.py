from setuptools import setup
setup(
    name='cli-anything-besu',
    version='1.0.0',
    packages=['cli_anything.besu'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-besu=cli_anything.besu:cli']},
)
