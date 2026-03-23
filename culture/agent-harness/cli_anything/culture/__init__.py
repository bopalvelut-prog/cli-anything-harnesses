import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('culture running')
@cli.command()
def start(): click.echo('culture started')
if __name__ == '__main__': cli()
