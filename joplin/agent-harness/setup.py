from setuptools import setup
setup(
    name='cli-anything-joplin',
    version='1.0.0',
    packages=['cli_anything.joplin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-joplin=cli_anything.joplin:cli']},
)
