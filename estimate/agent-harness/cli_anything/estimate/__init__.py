import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('estimate running')
@cli.command()
def start(): click.echo('estimate started')
if __name__ == '__main__': cli()
