from setuptools import setup
setup(
    name='cli-anything-wavelength',
    version='1.0.0',
    packages=['cli_anything.wavelength'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wavelength=cli_anything.wavelength:cli']},
)
