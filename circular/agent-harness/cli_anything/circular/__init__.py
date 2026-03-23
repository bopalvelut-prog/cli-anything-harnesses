import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('circular running')
@cli.command()
def start(): click.echo('circular started')
if __name__ == '__main__': cli()
