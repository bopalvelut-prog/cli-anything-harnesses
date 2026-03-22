from setuptools import setup
setup(
    name='cli-anything-openvpn',
    version='1.0.0',
    packages=['cli_anything.openvpn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openvpn=cli_anything.openvpn:cli']},
)
