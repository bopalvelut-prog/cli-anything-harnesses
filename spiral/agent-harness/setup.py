from setuptools import setup
setup(
    name='cli-anything-spiral',
    version='1.0.0',
    packages=['cli_anything.spiral'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spiral=cli_anything.spiral:cli']},
)
