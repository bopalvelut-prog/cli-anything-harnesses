from setuptools import setup
setup(
    name='cli-anything-mod_mono',
    version='1.0.0',
    packages=['cli_anything.mod_mono'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mod_mono=cli_anything.mod_mono:cli']},
)
