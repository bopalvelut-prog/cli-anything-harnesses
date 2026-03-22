import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): click.echo('NordPass login')
@cli.command()
def list(): click.echo('NordPass entries')
if __name__ == '__main__': cli()
