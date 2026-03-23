from setuptools import setup
setup(
    name='cli-anything-dhcp',
    version='1.0.0',
    packages=['cli_anything.dhcp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dhcp=cli_anything.dhcp:cli']},
)
