from setuptools import setup
setup(
    name='cli-anything-glance',
    version='1.0.0',
    packages=['cli_anything.glance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-glance=cli_anything.glance:cli']},
)
