import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('som running')
@cli.command()
def start(): click.echo('som started')
if __name__ == '__main__': cli()
