from setuptools import setup
setup(
    name='cli-anything-konnectivity',
    version='1.0.0',
    packages=['cli_anything.konnectivity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-konnectivity=cli_anything.konnectivity:cli']},
)
