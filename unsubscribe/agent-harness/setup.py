from setuptools import setup
setup(
    name='cli-anything-unsubscribe',
    version='1.0.0',
    packages=['cli_anything.unsubscribe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unsubscribe=cli_anything.unsubscribe:cli']},
)
