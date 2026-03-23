from setuptools import setup
setup(
    name='cli-anything-mediainfo',
    version='1.0.0',
    packages=['cli_anything.mediainfo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mediainfo=cli_anything.mediainfo:cli']},
)
