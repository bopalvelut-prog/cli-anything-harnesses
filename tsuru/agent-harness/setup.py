from setuptools import setup
setup(
    name='cli-anything-tsuru',
    version='1.0.0',
    packages=['cli_anything.tsuru'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tsuru=cli_anything.tsuru:cli']},
)
