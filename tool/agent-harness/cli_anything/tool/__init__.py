import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tool running')
@cli.command()
def start(): click.echo('tool started')
if __name__ == '__main__': cli()
