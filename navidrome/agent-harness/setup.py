from setuptools import setup
setup(
    name='cli-anything-navidrome',
    version='1.0.0',
    packages=['cli_anything.navidrome'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-navidrome=cli_anything.navidrome:cli']},
)
