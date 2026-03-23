import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('penalty running')
@cli.command()
def start(): click.echo('penalty started')
if __name__ == '__main__': cli()
