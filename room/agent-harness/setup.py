from setuptools import setup
setup(
    name='cli-anything-room',
    version='1.0.0',
    packages=['cli_anything.room'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-room=cli_anything.room:cli']},
)
