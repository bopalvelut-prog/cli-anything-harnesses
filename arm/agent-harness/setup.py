from setuptools import setup
setup(
    name='cli-anything-arm',
    version='1.0.0',
    packages=['cli_anything.arm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arm=cli_anything.arm:cli']},
)
