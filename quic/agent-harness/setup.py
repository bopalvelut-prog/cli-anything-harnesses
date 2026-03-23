from setuptools import setup
setup(
    name='cli-anything-quic',
    version='1.0.0',
    packages=['cli_anything.quic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quic=cli_anything.quic:cli']},
)
