from setuptools import setup
setup(
    name='cli-anything-openai_whisper',
    version='1.0.0',
    packages=['cli_anything.openai_whisper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openai_whisper=cli_anything.openai_whisper:cli']},
)
