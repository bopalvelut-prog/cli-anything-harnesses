from setuptools import setup
setup(
    name='cli-anything-tilt',
    version='1.0.0',
    packages=['cli_anything.tilt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tilt=cli_anything.tilt:cli']},
)
