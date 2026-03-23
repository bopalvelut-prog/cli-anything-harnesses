from setuptools import setup
setup(
    name='cli-anything-wasm',
    version='1.0.0',
    packages=['cli_anything.wasm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wasm=cli_anything.wasm:cli']},
)
