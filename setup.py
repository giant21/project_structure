import setuptools

setuptools.setup(
    name="project_structure",
    version="1.0.0",
    description="example of project structure",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"})
