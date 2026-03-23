from setuptools import setup
setup(
    name='cli-anything-llama_cpp',
    version='1.0.0',
    packages=['cli_anything.llama_cpp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-llama_cpp=cli_anything.llama_cpp:cli']},
)
