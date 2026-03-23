import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('developer running')
@cli.command()
def start(): click.echo('developer started')
if __name__ == '__main__': cli()
