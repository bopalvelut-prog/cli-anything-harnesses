import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bookworm running')
@cli.command()
def start(): click.echo('bookworm started')
if __name__ == '__main__': cli()
