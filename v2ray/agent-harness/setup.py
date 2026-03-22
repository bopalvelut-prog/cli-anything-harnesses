from setuptools import setup
setup(
    name='cli-anything-v2ray',
    version='1.0.0',
    packages=['cli_anything.v2ray'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-v2ray=cli_anything.v2ray:cli']},
)
