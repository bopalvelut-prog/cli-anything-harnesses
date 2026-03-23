from setuptools import setup
setup(
    name='cli-anything-unmount',
    version='1.0.0',
    packages=['cli_anything.unmount'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unmount=cli_anything.unmount:cli']},
)
