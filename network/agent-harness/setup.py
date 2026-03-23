from setuptools import setup
setup(
    name='cli-anything-network',
    version='1.0.0',
    packages=['cli_anything.network'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-network=cli_anything.network:cli']},
)
