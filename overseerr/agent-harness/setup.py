from setuptools import setup
setup(
    name='cli-anything-overseerr',
    version='1.0.0',
    packages=['cli_anything.overseerr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-overseerr=cli_anything.overseerr:cli']},
)
