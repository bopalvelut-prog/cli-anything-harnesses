import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('winter running')
@cli.command()
def start(): click.echo('winter started')
if __name__ == '__main__': cli()
