from setuptools import setup
setup(
    name='cli-anything-vllm',
    version='1.0.0',
    packages=['cli_anything.vllm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vllm=cli_anything.vllm:cli']},
)
