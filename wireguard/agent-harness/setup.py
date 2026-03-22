from setuptools import setup
setup(
    name='cli-anything-wireguard',
    version='1.0.0',
    packages=['cli_anything.wireguard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wireguard=cli_anything.wireguard:cli']},
)
