from setuptools import setup
setup(
    name='cli-anything-bridge',
    version='1.0.0',
    packages=['cli_anything.bridge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bridge=cli_anything.bridge:cli']},
)
