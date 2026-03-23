from setuptools import setup
setup(
    name='cli-anything-voice',
    version='1.0.0',
    packages=['cli_anything.voice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-voice=cli_anything.voice:cli']},
)
