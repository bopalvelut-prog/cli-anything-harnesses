import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tear running')
@cli.command()
def start(): click.echo('tear started')
if __name__ == '__main__': cli()
