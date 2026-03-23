from setuptools import setup
setup(
    name='cli-anything-wireguard_v4',
    version='1.0.0',
    packages=['cli_anything.wireguard_v4'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wireguard_v4=cli_anything.wireguard_v4:cli']},
)
