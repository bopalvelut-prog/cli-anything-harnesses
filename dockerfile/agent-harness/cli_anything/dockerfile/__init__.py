import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dockerfile running')
@cli.command()
def start(): click.echo('dockerfile started')
if __name__ == '__main__': cli()
