import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('messagebird running')
@cli.command()
def start(): click.echo('messagebird started')
if __name__ == '__main__': cli()
