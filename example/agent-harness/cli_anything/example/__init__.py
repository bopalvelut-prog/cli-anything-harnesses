import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('example running')
@cli.command()
def start(): click.echo('example started')
if __name__ == '__main__': cli()
