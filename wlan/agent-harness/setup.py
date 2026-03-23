from setuptools import setup
setup(
    name='cli-anything-wlan',
    version='1.0.0',
    packages=['cli_anything.wlan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wlan=cli_anything.wlan:cli']},
)
