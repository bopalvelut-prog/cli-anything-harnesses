import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('whale running')
@cli.command()
def start(): click.echo('whale started')
if __name__ == '__main__': cli()
