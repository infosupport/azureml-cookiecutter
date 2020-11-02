from setuptools import setup, find_packages


with open('README.rst', 'r') as readme_file:
    readme_content = readme_file.read()

with open('LICENSE', 'r') as license_file:
    license_content = license_file.read()

setup(
    name='{{cookiecutter.package_name}}',
    version='0.1.0',
    description='{{cookiecutter.project_name}}',
    long_description=readme_content,
    license=license_content,
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        # Add your dependencies here.
    ]
)
