from setuptools import setup
setup(
    name='cli-anything-scrcpy',
    version='1.0.0',
    packages=['cli_anything.scrcpy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scrcpy=cli_anything.scrcpy:cli']},
)
