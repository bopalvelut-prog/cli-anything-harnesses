from setuptools import setup
setup(
    name='cli-anything-vignette',
    version='1.0.0',
    packages=['cli_anything.vignette'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vignette=cli_anything.vignette:cli']},
)
