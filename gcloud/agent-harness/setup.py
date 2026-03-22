from setuptools import setup
setup(
    name='cli-anything-gcloud',
    version='1.0.0',
    packages=['cli_anything.gcloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcloud=cli_anything.gcloud:cli']},
)
