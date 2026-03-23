from setuptools import setup
setup(
    name='cli-anything-libuv',
    version='1.0.0',
    packages=['cli_anything.libuv'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-libuv=cli_anything.libuv:cli']},
)
