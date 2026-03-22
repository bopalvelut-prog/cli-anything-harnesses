import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['ceph', 'status'])
@cli.command()
def health(): subprocess.run(['ceph', 'health'])
if __name__ == '__main__': cli()
