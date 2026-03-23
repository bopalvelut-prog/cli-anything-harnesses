from setuptools import setup
setup(
    name='cli-anything-banner',
    version='1.0.0',
    packages=['cli_anything.banner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-banner=cli_anything.banner:cli']},
)
