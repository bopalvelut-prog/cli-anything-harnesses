from setuptools import setup
setup(
    name='cli-anything-jitsi',
    version='1.0.0',
    packages=['cli_anything.jitsi'],
    install_requires=['click', 'requests'],
    entry_points={'console_scripts': ['cli-anything-jitsi=cli_anything.jitsi:cli']},
)
