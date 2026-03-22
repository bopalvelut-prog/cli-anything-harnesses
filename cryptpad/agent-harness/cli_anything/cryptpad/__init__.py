import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('CryptPad running')
@cli.command()
def docs(): click.echo('CryptPad docs')
if __name__ == '__main__': cli()
