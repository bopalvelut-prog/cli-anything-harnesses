from setuptools import setup
setup(
    name='cli-anything-accelerate',
    version='1.0.0',
    packages=['cli_anything.accelerate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-accelerate=cli_anything.accelerate:cli']},
)
