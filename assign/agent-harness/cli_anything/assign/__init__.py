import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('assign running')
@cli.command()
def start(): click.echo('assign started')
if __name__ == '__main__': cli()
