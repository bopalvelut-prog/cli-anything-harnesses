from setuptools import setup
setup(
    name='cli-anything-ttyd',
    version='1.0.0',
    packages=['cli_anything.ttyd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ttyd=cli_anything.ttyd:cli']},
)
