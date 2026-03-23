from setuptools import setup
setup(
    name='cli-anything-quality',
    version='1.0.0',
    packages=['cli_anything.quality'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quality=cli_anything.quality:cli']},
)
