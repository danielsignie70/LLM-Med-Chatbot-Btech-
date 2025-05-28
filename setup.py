from setuptools import find_packages, setup

setup(
    name='Generative AI Project',
    version='0.0.0',
    author='Daniel SIGNIE',
    author_email='danielsignie#gmail.com',
    description='A brief description of your project',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, e.g.:
        'flask',
        'python-dotenv',
        'pinecone-client[grpc]',
        'langchain[pinecone]',
        'langchain[openai]',
        'langchain[community]',
        'langchain[experimental]',
    ],
)