from setuptools import setup
setup(
    name='cli-anything-dhclient',
    version='1.0.0',
    packages=['cli_anything.dhclient'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dhclient=cli_anything.dhclient:cli']},
)
