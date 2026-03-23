from setuptools import setup
setup(
    name='cli-anything-announcements',
    version='1.0.0',
    packages=['cli_anything.announcements'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-announcements=cli_anything.announcements:cli']},
)
