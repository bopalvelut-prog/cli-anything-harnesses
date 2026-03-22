from setuptools import setup
setup(
    name='cli-anything-plane',
    version='1.0.0',
    packages=['cli_anything.plane'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plane=cli_anything.plane:cli']},
)
