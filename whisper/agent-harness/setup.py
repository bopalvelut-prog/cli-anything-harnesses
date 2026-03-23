from setuptools import setup
setup(
    name='cli-anything-whisper',
    version='1.0.0',
    packages=['cli_anything.whisper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-whisper=cli_anything.whisper:cli']},
)
