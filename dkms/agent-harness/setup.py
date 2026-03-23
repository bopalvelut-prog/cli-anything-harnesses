from setuptools import setup
setup(
    name='cli-anything-dkms',
    version='1.0.0',
    packages=['cli_anything.dkms'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dkms=cli_anything.dkms:cli']},
)
