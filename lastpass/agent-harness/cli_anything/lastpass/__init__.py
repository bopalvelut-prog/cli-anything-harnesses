import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): click.echo('LastPass login')
@cli.command()
def list(): click.echo('LastPass entries')
if __name__ == '__main__': cli()
