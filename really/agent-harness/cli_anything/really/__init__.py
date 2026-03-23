import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('really running')
@cli.command()
def start(): click.echo('really started')
if __name__ == '__main__': cli()
