import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cable running')
@cli.command()
def start(): click.echo('cable started')
if __name__ == '__main__': cli()
