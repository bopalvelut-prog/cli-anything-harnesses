from setuptools import setup
setup(
    name='cli-anything-meilisearch',
    version='1.0.0',
    packages=['cli_anything.meilisearch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-meilisearch=cli_anything.meilisearch:cli']},
)
