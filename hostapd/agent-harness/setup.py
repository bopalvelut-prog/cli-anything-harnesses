from setuptools import setup
setup(
    name='cli-anything-hostapd',
    version='1.0.0',
    packages=['cli_anything.hostapd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hostapd=cli_anything.hostapd:cli']},
)
