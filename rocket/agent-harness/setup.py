from setuptools import setup
setup(
    name='cli-anything-rocket',
    version='1.0.0',
    packages=['cli_anything.rocket'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rocket=cli_anything.rocket:cli']},
)
