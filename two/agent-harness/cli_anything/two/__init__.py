import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('two running')
@cli.command()
def start(): click.echo('two started')
if __name__ == '__main__': cli()
