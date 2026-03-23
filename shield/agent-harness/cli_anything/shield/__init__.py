import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shield running')
@cli.command()
def start(): click.echo('shield started')
if __name__ == '__main__': cli()
