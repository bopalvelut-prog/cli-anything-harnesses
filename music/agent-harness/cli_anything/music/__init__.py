import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('music running')
@cli.command()
def start(): click.echo('music started')
if __name__ == '__main__': cli()
