from setuptools import setup
setup(
    name='cli-anything-music',
    version='1.0.0',
    packages=['cli_anything.music'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-music=cli_anything.music:cli']},
)
