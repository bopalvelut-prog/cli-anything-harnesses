from setuptools import setup
setup(
    name='cli-anything-amazon_transcribe',
    version='1.0.0',
    packages=['cli_anything.amazon_transcribe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_transcribe=cli_anything.amazon_transcribe:cli']},
)
