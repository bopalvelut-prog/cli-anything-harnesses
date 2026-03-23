from setuptools import setup
setup(
    name='cli-anything-elevenlabs',
    version='1.0.0',
    packages=['cli_anything.elevenlabs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-elevenlabs=cli_anything.elevenlabs:cli']},
)
