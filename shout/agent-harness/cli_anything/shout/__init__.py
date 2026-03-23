import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shout running')
@cli.command()
def start(): click.echo('shout started')
if __name__ == '__main__': cli()
