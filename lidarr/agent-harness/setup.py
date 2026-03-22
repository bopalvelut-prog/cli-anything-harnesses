from setuptools import setup
setup(
    name='cli-anything-lidarr',
    version='1.0.0',
    packages=['cli_anything.lidarr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lidarr=cli_anything.lidarr:cli']},
)
