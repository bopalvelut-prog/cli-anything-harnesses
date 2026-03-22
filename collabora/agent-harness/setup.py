from setuptools import setup
setup(
    name='cli-anything-collabora',
    version='1.0.0',
    packages=['cli_anything.collabora'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-collabora=cli_anything.collabora:cli']},
)
