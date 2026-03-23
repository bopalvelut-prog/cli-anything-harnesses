from setuptools import setup
setup(
    name='cli-anything-skywalking',
    version='1.0.0',
    packages=['cli_anything.skywalking'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-skywalking=cli_anything.skywalking:cli']},
)
