import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bay running')
@cli.command()
def start(): click.echo('bay started')
if __name__ == '__main__': cli()
