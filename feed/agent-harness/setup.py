from setuptools import setup
setup(
    name='cli-anything-feed',
    version='1.0.0',
    packages=['cli_anything.feed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-feed=cli_anything.feed:cli']},
)
