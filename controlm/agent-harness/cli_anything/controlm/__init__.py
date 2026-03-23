import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('controlm running')
@cli.command()
def start(): click.echo('controlm started')
if __name__ == '__main__': cli()
