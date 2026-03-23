from setuptools import setup
setup(
    name='cli-anything-nordvpn',
    version='1.0.0',
    packages=['cli_anything.nordvpn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nordvpn=cli_anything.nordvpn:cli']},
)
