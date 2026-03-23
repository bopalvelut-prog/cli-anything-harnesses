from setuptools import setup
setup(
    name='cli-anything-repost',
    version='1.0.0',
    packages=['cli_anything.repost'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-repost=cli_anything.repost:cli']},
)
