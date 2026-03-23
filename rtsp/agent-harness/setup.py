from setuptools import setup
setup(
    name='cli-anything-rtsp',
    version='1.0.0',
    packages=['cli_anything.rtsp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rtsp=cli_anything.rtsp:cli']},
)
