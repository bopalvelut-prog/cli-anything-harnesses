from setuptools import setup
setup(
    name='cli-anything-shadowsocks',
    version='1.0.0',
    packages=['cli_anything.shadowsocks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shadowsocks=cli_anything.shadowsocks:cli']},
)
