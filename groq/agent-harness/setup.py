from setuptools import setup
setup(
    name='cli-anything-groq',
    version='1.0.0',
    packages=['cli_anything.groq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-groq=cli_anything.groq:cli']},
)
