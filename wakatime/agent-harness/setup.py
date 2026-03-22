from setuptools import setup
setup(
    name='cli-anything-wakatime',
    version='1.0.0',
    packages=['cli_anything.wakatime'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wakatime=cli_anything.wakatime:cli']},
)
