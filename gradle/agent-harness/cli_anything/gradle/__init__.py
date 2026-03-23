import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gradle running')
@cli.command()
def start(): click.echo('gradle started')
if __name__ == '__main__': cli()
