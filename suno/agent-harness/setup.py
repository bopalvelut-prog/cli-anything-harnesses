from setuptools import setup
setup(
    name='cli-anything-suno',
    version='1.0.0',
    packages=['cli_anything.suno'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-suno=cli_anything.suno:cli']},
)
