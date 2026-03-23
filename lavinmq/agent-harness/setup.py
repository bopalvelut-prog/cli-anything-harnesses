from setuptools import setup
setup(
    name='cli-anything-lavinmq',
    version='1.0.0',
    packages=['cli_anything.lavinmq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lavinmq=cli_anything.lavinmq:cli']},
)
