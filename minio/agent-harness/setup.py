from setuptools import setup
setup(
    name='cli-anything-minio',
    version='1.0.0',
    packages=['cli_anything.minio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-minio=cli_anything.minio:cli']},
)
