import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('institution running')
@cli.command()
def start(): click.echo('institution started')
if __name__ == '__main__': cli()
