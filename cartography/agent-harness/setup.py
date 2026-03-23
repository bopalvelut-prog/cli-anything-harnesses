from setuptools import setup
setup(
    name='cli-anything-cartography',
    version='1.0.0',
    packages=['cli_anything.cartography'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cartography=cli_anything.cartography:cli']},
)
