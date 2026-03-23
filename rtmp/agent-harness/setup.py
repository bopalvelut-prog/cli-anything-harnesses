from setuptools import setup
setup(
    name='cli-anything-rtmp',
    version='1.0.0',
    packages=['cli_anything.rtmp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rtmp=cli_anything.rtmp:cli']},
)
