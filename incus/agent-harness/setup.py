from setuptools import setup
setup(
    name='cli-anything-incus',
    version='1.0.0',
    packages=['cli_anything.incus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-incus=cli_anything.incus:cli']},
)
