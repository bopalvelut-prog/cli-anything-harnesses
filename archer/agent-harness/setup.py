from setuptools import setup
setup(
    name='cli-anything-archer',
    version='1.0.0',
    packages=['cli_anything.archer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-archer=cli_anything.archer:cli']},
)
