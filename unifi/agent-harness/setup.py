from setuptools import setup
setup(
    name='cli-anything-unifi',
    version='1.0.0',
    packages=['cli_anything.unifi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unifi=cli_anything.unifi:cli']},
)
