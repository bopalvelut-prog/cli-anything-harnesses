import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grave running')
@cli.command()
def start(): click.echo('grave started')
if __name__ == '__main__': cli()
