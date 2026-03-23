from setuptools import setup
setup(
    name='cli-anything-uvicorn',
    version='1.0.0',
    packages=['cli_anything.uvicorn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-uvicorn=cli_anything.uvicorn:cli']},
)
