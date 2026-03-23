from setuptools import setup
setup(
    name='cli-anything-anythingllm',
    version='1.0.0',
    packages=['cli_anything.anythingllm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-anythingllm=cli_anything.anythingllm:cli']},
)
