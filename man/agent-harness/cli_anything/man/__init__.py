import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('man running')
@cli.command()
def start(): click.echo('man started')
if __name__ == '__main__': cli()
