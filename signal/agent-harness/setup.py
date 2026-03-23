from setuptools import setup
setup(
    name='cli-anything-signal',
    version='1.0.0',
    packages=['cli_anything.signal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-signal=cli_anything.signal:cli']},
)
