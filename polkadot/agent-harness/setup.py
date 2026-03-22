from setuptools import setup
setup(
    name='cli-anything-polkadot',
    version='1.0.0',
    packages=['cli_anything.polkadot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-polkadot=cli_anything.polkadot:cli']},
)
