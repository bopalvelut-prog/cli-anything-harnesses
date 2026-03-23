from setuptools import setup
setup(
    name='cli-anything-provision',
    version='1.0.0',
    packages=['cli_anything.provision'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-provision=cli_anything.provision:cli']},
)
