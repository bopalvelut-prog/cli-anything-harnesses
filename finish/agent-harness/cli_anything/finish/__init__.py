import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('finish running')
@cli.command()
def start(): click.echo('finish started')
if __name__ == '__main__': cli()
