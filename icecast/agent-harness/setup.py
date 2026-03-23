from setuptools import setup
setup(
    name='cli-anything-icecast',
    version='1.0.0',
    packages=['cli_anything.icecast'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-icecast=cli_anything.icecast:cli']},
)
