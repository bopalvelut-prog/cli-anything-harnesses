import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('severity running')
@cli.command()
def start(): click.echo('severity started')
if __name__ == '__main__': cli()
