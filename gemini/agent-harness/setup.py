from setuptools import setup
setup(
    name='cli-anything-gemini',
    version='1.0.0',
    packages=['cli_anything.gemini'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gemini=cli_anything.gemini:cli']},
)
