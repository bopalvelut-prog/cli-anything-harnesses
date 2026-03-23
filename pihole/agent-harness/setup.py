from setuptools import setup
setup(
    name='cli-anything-pihole',
    version='1.0.0',
    packages=['cli_anything.pihole'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pihole=cli_anything.pihole:cli']},
)
