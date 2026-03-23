import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scalability running')
@cli.command()
def start(): click.echo('scalability started')
if __name__ == '__main__': cli()
