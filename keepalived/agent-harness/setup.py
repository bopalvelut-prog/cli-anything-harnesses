from setuptools import setup
setup(
    name='cli-anything-keepalived',
    version='1.0.0',
    packages=['cli_anything.keepalived'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-keepalived=cli_anything.keepalived:cli']},
)
