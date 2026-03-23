import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('actiontext running')
@cli.command()
def start(): click.echo('actiontext started')
if __name__ == '__main__': cli()
