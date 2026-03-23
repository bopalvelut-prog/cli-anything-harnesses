from setuptools import setup
setup(
    name='cli-anything-unity',
    version='1.0.0',
    packages=['cli_anything.unity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unity=cli_anything.unity:cli']},
)
