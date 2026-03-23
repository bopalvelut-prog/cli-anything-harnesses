from setuptools import setup
setup(
    name='cli-anything-yt',
    version='1.0.0',
    packages=['cli_anything.yt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yt=cli_anything.yt:cli']},
)
