import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('huge running')
@cli.command()
def start(): click.echo('huge started')
if __name__ == '__main__': cli()
