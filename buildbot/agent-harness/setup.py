from setuptools import setup
setup(
    name='cli-anything-buildbot',
    version='1.0.0',
    packages=['cli_anything.buildbot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-buildbot=cli_anything.buildbot:cli']},
)
