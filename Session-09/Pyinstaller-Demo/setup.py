setup(
    name="python-installer-test",
    version="1.0.0",
    description="Testing the pyinstaller package.",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/adygcode/PythonInstallerTest",
    author="Adrian Gould",
    author_email="adrian.gould@nmtafe.wa.edu.au",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=[],
    include_package_data=True,
    install_requires=[
        "importlib_resources"
    ],
    entry_points={"console_scripts": ["realpython=application:main"]},
)