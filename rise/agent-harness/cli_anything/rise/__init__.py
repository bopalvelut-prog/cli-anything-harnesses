import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rise running')
@cli.command()
def start(): click.echo('rise started')
if __name__ == '__main__': cli()
