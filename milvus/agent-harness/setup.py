from setuptools import setup
setup(
    name='cli-anything-milvus',
    version='1.0.0',
    packages=['cli_anything.milvus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-milvus=cli_anything.milvus:cli']},
)
