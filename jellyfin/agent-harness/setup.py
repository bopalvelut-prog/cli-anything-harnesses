from setuptools import setup
setup(
    name='cli-anything-jellyfin',
    version='1.0.0',
    packages=['cli_anything.jellyfin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jellyfin=cli_anything.jellyfin:cli']},
)
