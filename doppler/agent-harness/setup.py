from setuptools import setup
setup(
    name='cli-anything-doppler',
    version='1.0.0',
    packages=['cli_anything.doppler'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-doppler=cli_anything.doppler:cli']},
)
