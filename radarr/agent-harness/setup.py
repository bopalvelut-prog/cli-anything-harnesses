from setuptools import setup
setup(
    name='cli-anything-radarr',
    version='1.0.0',
    packages=['cli_anything.radarr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-radarr=cli_anything.radarr:cli']},
)
