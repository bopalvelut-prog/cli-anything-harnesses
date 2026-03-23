from setuptools import setup
setup(
    name='cli-anything-follow',
    version='1.0.0',
    packages=['cli_anything.follow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-follow=cli_anything.follow:cli']},
)
