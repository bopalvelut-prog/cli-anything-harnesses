import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('genius running')
@cli.command()
def start(): click.echo('genius started')
if __name__ == '__main__': cli()
