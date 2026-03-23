from setuptools import setup
setup(
    name='cli-anything-texture',
    version='1.0.0',
    packages=['cli_anything.texture'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-texture=cli_anything.texture:cli']},
)
