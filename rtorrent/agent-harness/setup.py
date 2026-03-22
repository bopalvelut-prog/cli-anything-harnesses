from setuptools import setup
setup(
    name='cli-anything-rtorrent',
    version='1.0.0',
    packages=['cli_anything.rtorrent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rtorrent=cli_anything.rtorrent:cli']},
)
