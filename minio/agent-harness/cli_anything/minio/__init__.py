import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def server(): subprocess.run(['minio', 'server', '/data'])
@cli.command()
def client(): subprocess.run(['mc', 'ls'])
if __name__ == '__main__': cli()
