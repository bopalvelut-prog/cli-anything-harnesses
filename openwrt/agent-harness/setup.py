from setuptools import setup
setup(
    name='cli-anything-openwrt',
    version='1.0.0',
    packages=['cli_anything.openwrt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openwrt=cli_anything.openwrt:cli']},
)
