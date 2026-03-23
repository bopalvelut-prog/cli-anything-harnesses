from setuptools import setup
setup(
    name='cli-anything-bazel',
    version='1.0.0',
    packages=['cli_anything.bazel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bazel=cli_anything.bazel:cli']},
)
