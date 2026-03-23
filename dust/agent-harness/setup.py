from setuptools import setup
setup(
    name='cli-anything-dust',
    version='1.0.0',
    packages=['cli_anything.dust'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dust=cli_anything.dust:cli']},
)
