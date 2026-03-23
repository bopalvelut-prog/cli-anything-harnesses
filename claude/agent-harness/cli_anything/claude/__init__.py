import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('claude running')
@cli.command()
def start(): click.echo('claude started')
if __name__ == '__main__': cli()
