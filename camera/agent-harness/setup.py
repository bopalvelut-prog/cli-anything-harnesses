from setuptools import setup
setup(
    name='cli-anything-camera',
    version='1.0.0',
    packages=['cli_anything.camera'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-camera=cli_anything.camera:cli']},
)
