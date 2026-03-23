from setuptools import setup
setup(
    name='cli-anything-dependency_track',
    version='1.0.0',
    packages=['cli_anything.dependency_track'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dependency_track=cli_anything.dependency_track:cli']},
)
