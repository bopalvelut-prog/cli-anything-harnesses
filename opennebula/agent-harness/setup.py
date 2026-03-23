from setuptools import setup
setup(
    name='cli-anything-opennebula',
    version='1.0.0',
    packages=['cli_anything.opennebula'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opennebula=cli_anything.opennebula:cli']},
)
