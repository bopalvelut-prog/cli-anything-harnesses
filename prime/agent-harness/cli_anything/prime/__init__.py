import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prime running')
@cli.command()
def start(): click.echo('prime started')
if __name__ == '__main__': cli()
