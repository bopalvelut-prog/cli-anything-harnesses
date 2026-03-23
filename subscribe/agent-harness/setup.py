from setuptools import setup
setup(
    name='cli-anything-subscribe',
    version='1.0.0',
    packages=['cli_anything.subscribe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-subscribe=cli_anything.subscribe:cli']},
)
