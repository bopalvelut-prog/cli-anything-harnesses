import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Keybase running')
@cli.command()
def encrypt(): click.echo('Keybase encrypt')
if __name__ == '__main__': cli()
