from setuptools import setup
setup(
    name='cli-anything-ethereum',
    version='1.0.0',
    packages=['cli_anything.ethereum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ethereum=cli_anything.ethereum:cli']},
)
