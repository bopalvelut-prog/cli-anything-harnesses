import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bridge running')
@cli.command()
def start(): click.echo('bridge started')
if __name__ == '__main__': cli()
