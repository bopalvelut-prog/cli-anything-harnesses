from setuptools import setup
setup(
    name='cli-anything-openvpn_as',
    version='1.0.0',
    packages=['cli_anything.openvpn_as'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openvpn_as=cli_anything.openvpn_as:cli']},
)
