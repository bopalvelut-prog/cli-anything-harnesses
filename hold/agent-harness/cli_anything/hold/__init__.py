import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hold running')
@cli.command()
def start(): click.echo('hold started')
if __name__ == '__main__': cli()
