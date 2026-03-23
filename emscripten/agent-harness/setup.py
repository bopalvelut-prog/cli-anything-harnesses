from setuptools import setup
setup(
    name='cli-anything-emscripten',
    version='1.0.0',
    packages=['cli_anything.emscripten'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-emscripten=cli_anything.emscripten:cli']},
)
