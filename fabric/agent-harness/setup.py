from setuptools import setup
setup(
    name='cli-anything-fabric',
    version='1.0.0',
    packages=['cli_anything.fabric'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fabric=cli_anything.fabric:cli']},
)
