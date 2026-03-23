import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('meeting running')
@cli.command()
def start(): click.echo('meeting started')
if __name__ == '__main__': cli()
