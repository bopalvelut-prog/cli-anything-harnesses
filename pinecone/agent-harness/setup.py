from setuptools import setup
setup(
    name='cli-anything-pinecone',
    version='1.0.0',
    packages=['cli_anything.pinecone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pinecone=cli_anything.pinecone:cli']},
)
