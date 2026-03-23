from setuptools import setup
setup(
    name='cli-anything-asr',
    version='1.0.0',
    packages=['cli_anything.asr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-asr=cli_anything.asr:cli']},
)
