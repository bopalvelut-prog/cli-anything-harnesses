import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lesson running')
@cli.command()
def start(): click.echo('lesson started')
if __name__ == '__main__': cli()
