from setuptools import setup
setup(
    name='cli-anything-sabnzbd',
    version='1.0.0',
    packages=['cli_anything.sabnzbd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sabnzbd=cli_anything.sabnzbd:cli']},
)
