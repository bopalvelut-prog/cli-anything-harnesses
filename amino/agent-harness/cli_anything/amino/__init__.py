import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amino running')
@cli.command()
def start(): click.echo('amino started')
if __name__ == '__main__': cli()
