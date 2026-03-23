import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('guardian running')
@cli.command()
def start(): click.echo('guardian started')
if __name__ == '__main__': cli()
