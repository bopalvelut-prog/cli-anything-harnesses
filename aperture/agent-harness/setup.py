from setuptools import setup
setup(
    name='cli-anything-aperture',
    version='1.0.0',
    packages=['cli_anything.aperture'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aperture=cli_anything.aperture:cli']},
)
