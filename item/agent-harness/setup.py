from setuptools import setup
setup(
    name='cli-anything-item',
    version='1.0.0',
    packages=['cli_anything.item'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-item=cli_anything.item:cli']},
)
