from setuptools import setup
setup(
    name='cli-anything-vlc',
    version='1.0.0',
    packages=['cli_anything.vlc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vlc=cli_anything.vlc:cli']},
)
