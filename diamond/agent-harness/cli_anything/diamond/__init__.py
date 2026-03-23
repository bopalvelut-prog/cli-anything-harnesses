import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('diamond running')
@cli.command()
def start(): click.echo('diamond started')
if __name__ == '__main__': cli()
