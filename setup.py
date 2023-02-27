import setuptools

setuptools.setup(
    name="gae-py27-sdk-box",
    version="0.1.0",
    py_modules=['gae_py27_sdk_box'],
    python_requires='>=2.6, <3',
    install_requires=[],
    include_package_data=True,
    data_files=[
        ('gae-py27-sdk-box', ['py27-gae-sdk-stipped.zip'])
    ],
)
