import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nipap running')
@cli.command()
def start(): click.echo('nipap started')
if __name__ == '__main__': cli()
