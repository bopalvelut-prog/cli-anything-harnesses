import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rudderstack running')
@cli.command()
def start(): click.echo('rudderstack started')
if __name__ == '__main__': cli()
