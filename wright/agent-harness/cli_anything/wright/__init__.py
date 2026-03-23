import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wright running')
@cli.command()
def start(): click.echo('wright started')
if __name__ == '__main__': cli()
