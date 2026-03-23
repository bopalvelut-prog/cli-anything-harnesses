from setuptools import setup
setup(
    name='cli-anything-weaviate_v3',
    version='1.0.0',
    packages=['cli_anything.weaviate_v3'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-weaviate_v3=cli_anything.weaviate_v3:cli']},
)
