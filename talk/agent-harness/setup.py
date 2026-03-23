from setuptools import setup
setup(
    name='cli-anything-talk',
    version='1.0.0',
    packages=['cli_anything.talk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-talk=cli_anything.talk:cli']},
)
