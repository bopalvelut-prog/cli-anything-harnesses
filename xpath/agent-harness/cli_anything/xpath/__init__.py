import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xpath running')
@cli.command()
def start(): click.echo('xpath started')
if __name__ == '__main__': cli()
