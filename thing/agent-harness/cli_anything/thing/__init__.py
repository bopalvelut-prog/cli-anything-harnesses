import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thing running')
@cli.command()
def start(): click.echo('thing started')
if __name__ == '__main__': cli()
