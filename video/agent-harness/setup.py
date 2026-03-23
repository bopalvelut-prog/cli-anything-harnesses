from setuptools import setup
setup(
    name='cli-anything-video',
    version='1.0.0',
    packages=['cli_anything.video'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-video=cli_anything.video:cli']},
)
