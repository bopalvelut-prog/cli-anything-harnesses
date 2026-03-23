import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('strand running')
@cli.command()
def start(): click.echo('strand started')
if __name__ == '__main__': cli()
