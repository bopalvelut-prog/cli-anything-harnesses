import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('folk running')
@cli.command()
def start(): click.echo('folk started')
if __name__ == '__main__': cli()
