import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('poetry running')
@cli.command()
def start(): click.echo('poetry started')
if __name__ == '__main__': cli()
