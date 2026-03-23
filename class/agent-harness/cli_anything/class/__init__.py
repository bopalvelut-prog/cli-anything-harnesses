import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('class running')
@cli.command()
def start(): click.echo('class started')
if __name__ == '__main__': cli()
