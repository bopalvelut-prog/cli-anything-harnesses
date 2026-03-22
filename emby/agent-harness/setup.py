from setuptools import setup
setup(
    name='cli-anything-emby',
    version='1.0.0',
    packages=['cli_anything.emby'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-emby=cli_anything.emby:cli']},
)
