import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def exports(): click.echo('NFS exports')
@cli.command()
def mounts(): click.echo('NFS mounts')
if __name__ == '__main__': cli()
