import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pressure running')
@cli.command()
def start(): click.echo('pressure started')
if __name__ == '__main__': cli()
