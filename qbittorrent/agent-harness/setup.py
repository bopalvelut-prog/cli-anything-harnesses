from setuptools import setup
setup(
    name='cli-anything-qbittorrent',
    version='1.0.0',
    packages=['cli_anything.qbittorrent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-qbittorrent=cli_anything.qbittorrent:cli']},
)
