from setuptools import setup
setup(
    name='cli-anything-openvswitch',
    version='1.0.0',
    packages=['cli_anything.openvswitch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openvswitch=cli_anything.openvswitch:cli']},
)
