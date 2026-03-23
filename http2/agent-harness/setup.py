from setuptools import setup
setup(
    name='cli-anything-http2',
    version='1.0.0',
    packages=['cli_anything.http2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-http2=cli_anything.http2:cli']},
)
