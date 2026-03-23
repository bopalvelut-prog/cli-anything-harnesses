from setuptools import setup
setup(
    name='cli-anything-luci',
    version='1.0.0',
    packages=['cli_anything.luci'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-luci=cli_anything.luci:cli']},
)
