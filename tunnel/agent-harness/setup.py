from setuptools import setup
setup(
    name='cli-anything-tunnel',
    version='1.0.0',
    packages=['cli_anything.tunnel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tunnel=cli_anything.tunnel:cli']},
)
