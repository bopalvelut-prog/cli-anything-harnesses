from setuptools import setup
setup(
    name='cli-anything-weaviate',
    version='1.0.0',
    packages=['cli_anything.weaviate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-weaviate=cli_anything.weaviate:cli']},
)
