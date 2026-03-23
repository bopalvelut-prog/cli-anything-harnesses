from setuptools import setup
setup(
    name='cli-anything-gaze',
    version='1.0.0',
    packages=['cli_anything.gaze'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gaze=cli_anything.gaze:cli']},
)
