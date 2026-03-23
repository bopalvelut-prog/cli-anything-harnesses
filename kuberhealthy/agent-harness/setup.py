from setuptools import setup
setup(
    name='cli-anything-kuberhealthy',
    version='1.0.0',
    packages=['cli_anything.kuberhealthy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kuberhealthy=cli_anything.kuberhealthy:cli']},
)
