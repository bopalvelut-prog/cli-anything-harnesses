from setuptools import setup
setup(
    name='cli-anything-walk',
    version='1.0.0',
    packages=['cli_anything.walk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-walk=cli_anything.walk:cli']},
)
